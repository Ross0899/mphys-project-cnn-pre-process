import tensorflow as tf
from tensorflow.keras.layers.experimental import preprocessing 

import tensorflow_datasets as tfds
from tensorflow_examples.models.pix2pix import pix2pix

import sklearn

import matplotlib

import glob
import os
import numpy 
import cv2

print(f"tensorflow={tf.__version__}")
print(f"tfds={tfds.__version__}")
# print(f"tensorflow_examples {tensorflow_examples.__version__}")
print(f"sklearn={sklearn.__version__}")
print(f"matplotlib={matplotlib.__version__}")
#print(f"glob {glob.__version__}")
print(f"numpy={numpy.__version__}")
print(f"cv2={cv2.__version__}")