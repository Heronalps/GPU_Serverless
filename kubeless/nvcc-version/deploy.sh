#!/bin/bash

kubeless function deploy nvcc-version --runtime gpupython3.7 \
                                  --from-file handler.py \
                                  --handler handler.handler