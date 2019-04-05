#!/bin/bash

kubeless function deploy matmul-tf --runtime gpupython3.7 \
                                  --from-file handler.py \
                                  --handler handler.handler