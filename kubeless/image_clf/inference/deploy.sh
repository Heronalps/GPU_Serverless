#!/bin/bash
kubeless function delete image-clf-inf37
sleep 3
kubeless function deploy image-clf-inf37 --runtime gpupython3.7 \
                                         --from-file image_clf_inf.py \
                                         --handler image_clf_inf.handler \
                                         --timeout 3600 

kubeless function delete image-clf-inf
sleep 3
kubeless function deploy image-clf-inf  --runtime gpupython3.6 \
                                        --from-file image_clf_inf.py \
                                        --handler image_clf_inf.handler \
                                        --timeout 3600 