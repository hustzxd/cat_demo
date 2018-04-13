#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in data/ilsvrc12
HOME=/home/zhaoxiandong/

DATA=./cat_data
TOOLS=$HOME/caffe/build/tools

$TOOLS/compute_image_mean $DATA/train_lmdb \
  $DATA/mean.binaryproto

echo "Done."