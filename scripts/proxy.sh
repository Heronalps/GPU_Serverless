#!bin/bash

# kubectl proxy -p 8080 &

# kubectl port-forward hello-6b9795899b-dmsv8 8080

curl -L --data '{"Racelab": "Serverless GPU\n"}' \
  --header "Content-Type:application/json" \
  localhost:8080/api/v1/racelab/default/services/hello:http-function-port/proxy/