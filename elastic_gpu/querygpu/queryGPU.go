package main

import (
	"context"
	"fmt"
	"log"
	"time"

	clientapi "github.com/prometheus/client_golang/api"
	prometheus "github.com/prometheus/client_golang/api/prometheus/v1"
	"github.com/prometheus/common/model"
	"github.com/spf13/viper"
)

func main() {
	// Watching namespaces usage
	client, err := clientapi.NewClient(clientapi.Config{Address: "https://prometheus.nautilus.optiputer.net"})
	if err != nil {
		log.Printf("%v", err)
		return
	}

	q := prometheus.NewAPI(client)

	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	// Query(ctx context.Context, query string, ts time.Time) (model.Value, api.Error)
	// curVal => model.Value
	if curVal, err := q.Query(ctx, "avg_over_time(namespace_gpu_utilization[1m])", time.Now()); err != nil {
		log.Printf("%v", err)
	} else {

		switch {
		case curVal.Type() == model.ValVector:
			vectorVal := curVal.(model.Vector)
			fmt.Println("===Vector====")
			fmt.Println(vectorVal)
			for _, elem := range vectorVal {
				for _, ns := range viper.GetStringSlice("portal.gpu_exceptions") {
					if string(elem.Metric["namespace_name"]) == ns {
						return
					}
				}
				if elem.Value < 10 {
					fmt.Println("GPU Utilization greater than 10")
				}

				if elem.Value < 20 {
					fmt.Println("GPU Utilization less than 20")
				}
			}
		}
	}
}
