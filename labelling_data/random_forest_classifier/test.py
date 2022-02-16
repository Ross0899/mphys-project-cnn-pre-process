import os
import cv2
import numpy as np

path1 = "../tem_images_to_be_classified/masks/" # colourful
path2 = "./data/divided/masks/" # greyscale from apeer


masks_list1 = []
masks_list2 = []

mask1 = cv2.imread(path1 + os.listdir(path1)[:1][0])
mask2 = cv2.imread(path2 + os.listdir(path2)[:1][0])

print(np.unique(mask1))
print(np.unique(mask2))