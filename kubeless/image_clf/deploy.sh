#!/bin/bash
kubeless function delete image-clf-train
sleep 3
kubeless function deploy image-clf-train --runtime gpupython3.7 \
                                         --from-file image_clf_train.py \
                                         --handler image_clf_train.handler \
                                         --timeout 3600 
sleep 3
kubeless function delete image-clf-inf
sleep 3
kubeless function deploy image-clf-inf --runtime gpupython3.7 \
                                       --from-file image_clf_inf.py \
                                       --handler image_clf_inf.handler \
                                       --timeout 3600 
                                       