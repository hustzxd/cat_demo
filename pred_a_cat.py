# -*- coding: utf-8 -*-
import sys
import os
import time

import caffe
import numpy as np

# If you get "No module named _caffe", either you have not built pycaffe or you have the wrong path.


def pred_img(model_def, model_weights, image_name):
    if not os.path.exists(model_def):
        print('{} does not exist.'.format(model_def))
        exit(1)
    if not os.path.exists(model_weights):
        print('{} does not exist.'.format(model_weights))
        exit(1)
    if not os.path.exists(image_name):
        print('{} does not exist.'.format(image_name))
        exit(1)

    # caffe.set_mode_cpu()
    caffe.set_device(0)  # if we have multiple GPUs, pick the first one
    caffe.set_mode_gpu()

    net = caffe.Net(model_def,  # defines the structure of the model
                    model_weights,  # contains the trained weights
                    caffe.TEST)  # use test mode (e.g., don't perform dropout)
    # load the mean ImageNet image (as distributed with Caffe) for subtraction

    mu = np.array([150, 170, 188])
    mu = mu / 256.0
    # npy_mean = npy_mean.mean(1).mean(1)  # average over pixels to obtain the mean (BGR) pixel values
    # print npy_mean
    print('mean-subtracted values:{}'.format(zip('BGR', mu)))

    # create transformer for the input called 'data'
    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})

    transformer.set_transpose('data', (2, 0, 1))  # move image channels to outermost dimension
    transformer.set_mean('data', mu)  # subtract the dataset-mean value in each channel
    # transformer.set_raw_scale('data', 255)  # rescale from [0, 1] to [0, 255]
    transformer.set_channel_swap('data', (2, 1, 0))  # swap channels from RGB to BGR

    image = caffe.io.load_image(image_name)
    transformed_image = transformer.preprocess('data', image)
    # copy the image data into the memory allocated for the net
    net.blobs['data'].data[...] = transformed_image

    # perform classification
    output = net.forward()
    output_prob = output['prob'][0]  # the output probability vector for the first image in the batch
    print('image_name: {}'.format(image_name))
    print('Predict result: {}'.format(words_list[output_prob.argmax()]))


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: python [deploy.prototxt] [caffemodel] [image_name]')
        exit(1)
    words_list = ['cat0(real)', 'cat1(not real)']
    start = time.time()
    pred_img(sys.argv[1], sys.argv[2], sys.argv[3])
    end = time.time()
    print('time: {}s'.format(end - start))
