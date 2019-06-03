for i in {0..9}
do

IMG_PER_EPOCH=$(echo "2^$i" | bc)
echo "$IMG_PER_EPOCH" | bc
done