#!/bin/bash

# kubeless function deploy hello --runtime python3.6 \
#                                 --from-file hello.py \
#                                 --handler hello.hello

kubeless function deploy gpu-test --runtime gpupython3.7 \
                                  --from-file gpu-test.py \
                                  --handler gpu-test.handler