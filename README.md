# GPU_Serverless

### Kubeless Request GPU

- Deploy the function 
``` 
kubeless function deploy <function-name> --runtime gpupython3.7 \
                                  --from-file <python-file> \
                                  --handler <handler-name> \
                                  --timeout <timeout-in-secs>  
```

- Request GPU
```
kubectl edit function <function-name>
```
Add up to 8 requested GPUs to the resource configuration file
```
resources:
    requests:
        nvidia.com/gpu: <number>
    limits:
        nvidia.com/gpu: <number>
```


### Mount volume/secret to kubeless function

``` kubectl edit function <function-name> ```

```
deployment:
     metadata:
       creationTimestamp: null
     spec:
       strategy: {}
       template:
         metadata:
           creationTimestamp: null
         spec:
           containers:
           - imagePullPolicy: Always
             name: ""
             resources: {}
             volumeMounts:
             - mountPath: /imageclf
               name: imageclf
           volumes:
           - name: imageclf
             secret:
               secretName: imageclf
```

### Kubernetes command

```
k get pods -n kubeless

k logs kubeless-controller-manager-56cbb7c58b-j66s9 -c kubeless-function-controller -n kubeless

http-trigger-controller

k delete pod kubeless-controller-manager-56cbb7c58b-j66s9 -n kubeless

k get configmap -n kubeless -o yaml > output.yaml

k edit configmap kubeless-config -n kubeless

```