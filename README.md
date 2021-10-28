# Deep Learning Images of Nano-sized Particles

## Preprocessing 
- Generate synthetic images & masks
- Overlay images & masks as a qualitative check
- Divide 512x512 images into 128x128 patches
- Augment patches using image transformations

To generate the synthetic training images and pre-process them, run the shell script:

    ./preprocess.sh [#images]

where __#images__ is the number of full-size 512x512 images to be generated.

The training images & masks for the deep learning algorithm are saved to: "./preprocessing/data/augmented/".