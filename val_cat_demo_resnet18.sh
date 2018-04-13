#!/usr/bin/env sh
set -e

HOME=/home/zhaoxiandong
TOOLS=$HOME/caffe/build/tools

# WEIGHTS=$HOME/data/bvlc_reference_caffenet.caffemodel
MODEL=./models/resnet18/train_val.prototxt
$TOOLS/caffe test \
    --model=$MODEL \
    --weights=$1 \
    --iterations=10 \
    --gpu=1