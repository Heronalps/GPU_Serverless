#!/bin/bash
kubeless function delete mnist-tf
sleep 1
kubeless function deploy mnist-tf --runtime gpupython3.7 \
                                  --from-file mnisttf.py \
                                  --handler mnisttf.handler \
                                  --timeout 3600