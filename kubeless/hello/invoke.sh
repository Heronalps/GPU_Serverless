for i in {0..9}

do
num_image=$(echo "2^$i"|bc)
echo $num_image
DATA_STRING=$(jq -n --arg ni "$num_image" '{"num_image":$ni}')
kubeless function call hello --data $DATA_STRING

done