#!bin/bash

# Iterate 10 times
# for i in {0..9}

# One time
for i in {0}

do
IMAGE_PATH="/racelab/SantaCruzIsland_Validation_5Class/Birds/IMG_1304.JPG"
NUM_IMAGE=10

DATA_STRING=$(jq -n --arg pt "$IMAGE_PATH" --arg ni "$NUM_IMAGE" '{"path":$pt, "num_image":$ni}')

#echo "$DATA_STRING"
echo "36"
kubeless function call image-clf-inf --data "$DATA_STRING"
echo "37"
kubeless function call image-clf-inf37 --data "$DATA_STRING"

done