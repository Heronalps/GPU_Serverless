#!/bin/bash
kubeless function delete iris37
sleep 1
kubeless function deploy iris37 --runtime gpupython3.7 \
                                --from-file iris.py \
                                --handler iris.handler \
                                --timeout 3600

kubeless function delete iris
sleep 1
kubeless function deploy iris --runtime gpupython3.6 \
                              --from-file iris.py \
                              --handler iris.handler \
                              --timeout 3600