#!/bin/bash

kubeless function deploy mnist-tf --runtime gpupython3.7 \
                                  --from-file mnisttf.py \
                                  --handler mnisttf.handler