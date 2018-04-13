# cat_demo

### data

- [augmentation](https://github.com/aleju/imgaug)

- generate lmdb

```
cd data
python get_list.py cat_data
./gen_lmdb.sh
./cal_mean.sh
```

### train

```
./train_cat_demo_resnet18.sh
```

### val

```
./val_cat_demo_resnet18.sh models/resnet18/cat-demo_iter_1000.caffemodel
```

### test one picture

```
python pred_a_cat.py models/resnet18/deploy.prototxt models/resnet18/cat-demo_iter_1000.caffemodel data/cat_data/test/cat0/05.jpg
```