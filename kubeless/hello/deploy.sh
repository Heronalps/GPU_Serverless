#!/bin/bash
kubeless function delete hello
sleep 3
kubeless function deploy hello --runtime python3.6 \
                                --from-file hello.py \
                                --handler hello.hello