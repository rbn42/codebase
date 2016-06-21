
import numpy as np
import matplotlib.pyplot as plt

import sys
# this file should be run from {caffe_root}/examples (otherwise change
# this line)
caffe_root = '../'
sys.path.insert(0, caffe_root + 'python')

import caffe

import os
if os.path.isfile(caffe_root + 'models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel'):
    print('CaffeNet found.')
else:
    print('Downloading pre-trained CaffeNet model...')
    # !../scripts/download_model_binary.py ../models/bvlc_reference_caffenet
