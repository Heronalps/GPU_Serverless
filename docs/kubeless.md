### Deploy Kubeless GPU container on Nautilus

1. Write lambda function with format as below:

```
def handler(event, context):
    return event
```

2. Create kubeless function by:

```
kubeless function deploy gpu-test --runtime gpupython3.7 \
                                  --from-file gpu-test.py \
                                  --handler gpu-test.handler
```
The runtime needs to be ```gpupython3.7```

3. Modify the GPU request in function manifesto by: 
```
kubectl edit functioni <function-name>
```
Add resource request:
```
resources:
    limits:
        nvidia.com/gpu: 1
    requests:
        nvidia.com/gpu: 1
```
