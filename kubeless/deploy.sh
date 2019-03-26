#!/bin/bash

kubeless function deploy hello --runtime python3.6 \
                                --from-file hello.py \
                                --handler hello.hello