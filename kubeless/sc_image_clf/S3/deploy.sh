#!/bin/bash
kubeless function delete sc_image_clf_train
sleep 1
kubeless function deploy sc_image_clf_train --runtime gpupython3.7 \
                                            --from-file image_clf_train.py \
                                            --handler image_clf_train.handler \
                                            --timeout 3600
sleep 1
kubeless function delete sc_image_clf_inf
sleep 1
kubeless function deploy sc_image_clf_inf --runtime gpupython3.7 \
                                          --from-file image_clf_inf.py \
                                          --handler image_clf_inf.handler \
                                          --timeout 3600