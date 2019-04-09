#!/bin/bash
kubeless function delete iris
sleep 1
kubeless function deploy iris --runtime gpupython3.7 \
                              --from-file iris.py \
                              --handler iris.handler \
                              --timeout 3600