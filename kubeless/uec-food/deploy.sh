#!/bin/bash

kubeless function deploy uec-food --runtime gpupython3.7 \
                                  --from-file handler.py \
                                  --handler handler.handler