#!/bin/bash
kubeless function delete mnist-cnn
sleep 2
kubeless function deploy mnist-cnn --runtime gpupython3.7 \
                                   --from-file mnist_cnn.py \
                                   --handler mnist_cnn.handler \
                                   --timeout 3600

kubeless function delete mnist-cnn-avx
sleep 2
kubeless function deploy mnist-cnn-avx --runtime gpupython3.6 \
                                   --from-file mnist_cnn.py \
                                   --handler mnist_cnn.handler \
                                   --timeout 3600