#!/bin/bash
kubeless function delete image-clf-train37
sleep 3
kubeless function deploy image-clf-train37 --runtime gpupython3.7 \
                                           --from-file image_clf_train.py \
                                           --handler image_clf_train.handler \
                                           --timeout 10800
sleep 3
sh patch-37.sh

kubeless function delete image-clf-train
sleep 3
kubeless function deploy image-clf-train  --runtime gpupython3.6 \
                                          --from-file image_clf_train.py \
                                          --handler image_clf_train.handler \
                                          --timeout 10800
sleep 3
sh patch.sh                                    