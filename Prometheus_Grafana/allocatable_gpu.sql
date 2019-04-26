avg without(instance, pod)(kube_node_status_allocatable{resource="nvidia_com_gpu"}) - on(node) 
  (sum(kube_pod_container_resource_requests{resource="nvidia_com_gpu"}) by(node) or on(node) 
    avg without(instance, pod)(kube_node_status_allocatable{resource="nvidia_com_gpu"})*0)