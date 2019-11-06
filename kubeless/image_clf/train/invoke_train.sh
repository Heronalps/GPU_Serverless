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

# Iterate 10 times
# for i in {0..9}

# One time
for i in {0}

do
IMG_PER_EPOCH=100
EPOCHS=1
#echo "$IMG_PER_EPOCH"
DATA_STRING=$(jq -n --arg ipe "$IMG_PER_EPOCH" '{"img_per_epoch":$ipe}' --arg ep "$EPOCHS" '{"num_epoch":$ep}')
#echo "$DATA_STRING"
kubeless function call image-clf-train --data "$DATA_STRING"

# kubeless function call image-clf-train37 --data "$DATA_STRING"

done