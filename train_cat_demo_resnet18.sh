#!/usr/bin/env sh
set -e

HOME=/home/zhaoxiandong
TOOLS=$HOME/caffe/build/tools
cur_date=`date +%Y:%m:%d-%H:%M:%S`
cur_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
log_file_name="$cur_dir/log/cat_demo_resnet18-${cur_date}.log"

solver=models/resnet18/solver.prototxt
$TOOLS/caffe train \
    --solver=$solver \
    --weights=$1 \
    --gpu=1 2>&1 | tee -a ${log_file_name}