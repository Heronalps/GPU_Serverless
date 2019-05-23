#!bin/bash

# Newborn Pod needs to probe for downloading imagenet model
#kubeless function call image-clf-train --data '{"img_per_epoch":"10"}'

# for i in {0..7}

# do
# IMG_PER_EPOCH=$(echo "2^$i*10"|bc)
# #echo "$IMG_PER_EPOCH"
# DATA_STRING=$(jq -n --arg ipe "$IMG_PER_EPOCH" '{"img_per_epoch":$ipe}')
# #echo "$DATA_STRING"
# kubeless function call image-clf-train --data "$DATA_STRING"

# done

for i in {0..9}

do
IMG_PER_EPOCH=100
#echo "$IMG_PER_EPOCH"
DATA_STRING=$(jq -n --arg ipe "$IMG_PER_EPOCH" '{"img_per_epoch":$ipe}')
#echo "$DATA_STRING"
kubeless function call image-clf-train --data "$DATA_STRING"

done