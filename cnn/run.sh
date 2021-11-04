#!/bin/sh

#$ -cwd
#$ -N CNN-training-v2
#$ -m be
pip install tensorflow
pip install -q git+https://github.com/tensorflow/examples.git

python3 cnn_v2_training.py
