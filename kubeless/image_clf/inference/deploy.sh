#!/bin/bash
# kubeless function delete image-clf-inf37
# sleep 3
# kubeless function deploy image-clf-inf37 --runtime gpupython3.7 \
#                                          --from-file image_clf_inf.py \
#                                          --handler image_clf_inf.handler \
#                                          --timeout 10800
# sleep 3
# sh patch-37.sh

kubeless function delete image-clf-inf
sleep 3
kubeless function deploy image-clf-inf  --runtime gpupython3.6 \
                                        --from-file image_clf_inf.py \
                                        --handler image_clf_inf.handler \
                                        --timeout 10800
sleep 3
sh patch.sh                                                                            