#!/bin/bash

kubeless function deploy gpu-test --runtime gpupython3.7 \
                                  --from-file gpu-test.py \
                                  --handler gpu-test.handler