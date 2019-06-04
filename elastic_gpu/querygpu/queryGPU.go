package main

import (
	"context"
	"fmt"
	"log"
	"time"

	"github.com/prometheus/client_golang/api/prometheus/"
	"github.com/prometheus/common/model"
	"github.com/spf13/viper"
)

func main() {
	// Watching namespaces usage
	client, err := prometheus.New(peometheus.Config{Address: "https://prometheus.nautilus.optiputer.net"})
	if err != nil {
		log.Printf("%v", err)
		return
	}

	q := prometheus.NewQueryAPI(client)

	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	checkNs := func() {
		if curVal, err := q.Query(ctx, "avg_over_time(namespace_gpu_utilization[6h])", time.Now()); err != nil {
			log.Printf("%v", err)
		} else {
			switch {
			case curVal.Type() == model.ValVector:
				vectorVal := curVal.(model.Vector)

				for _, elem := range vectorVal {
					for _, ns := range viper.GetStringSlice("portal.gpu_exceptions") {
						if string(elem.Metric["namespace_name"]) == ns {
							return
						}
					}

					severity := "warning"
					if elem.Value < 10 {
						severity = "alert"
					}

					if elem.Value < 20 {
						botherUsersAboutNamespace(getNamespaceUsers(string(elem.Metric["namespace_name"])), string(elem.Metric["namespace_name"]), float32(elem.Value), severity)
					}
				}
			}
		}
	}
}

func botherUsersAboutNamespace(destination []string, namespace string, value float32, severity string) {
	botherTimeBytes, _ := time.Now().MarshalText()
	nsBothered[namespace] = fmt.Sprintf("%s", botherTimeBytes)
	destination = append(destination, "Michael Zhang <lebo@ucsb.edu>")
	r := NewMailRequest(destination, "Nautilus cluster "+severity+": Namespace GPUs utilization")

	err := r.parseTemplate("templates/nsmail.tmpl", "nsmail.tmpl", map[string]interface{}{
		"namespace": namespace,
		"value":     value,
		"severity":  severity,
	})
	if err != nil {
		log.Printf("Error parsing the email template: %s", err.Error())
	}

	if err := r.sendMail(); err != nil {
		log.Printf("Failed to send the email to %s : %s\n", r.to, err.Error())
	}
}
