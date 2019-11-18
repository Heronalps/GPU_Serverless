#!bin/bash

# Iterate 10 times
# for i in {0..9}

# One time
for i in {1..10}

do
NUM_IMAGE=$(echo "$i*10" | bc)

DATA_STRING=$(jq -n --arg ni "$NUM_IMAGE" '{"num_image":$ni}')
echo $DATA_STRING

echo "36"
kubeless function call image-clf-inf --data "$DATA_STRING"
# echo "37"
# kubeless function call image-clf-inf37 --data "$DATA_STRING"

done