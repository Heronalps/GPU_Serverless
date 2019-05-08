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
             - mountPath: /var/run/secrets
               name: s3-cred
               readOnly: true
           volumes:
           - name: s3-cred
             secret:
               secretName: s3-cred
```