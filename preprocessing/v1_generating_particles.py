# -*- coding: utf-8 -*-
"""
Created on Sun 6 Oct 2019

Python code for generating simulated image of randomly placed, potentially overlapping particles with random radii.

It is probably better/faster to do this with masks,
but the code below works for the intended purpose and is fast enough

@author: jobthijssen
"""

# import required packages
import imageio as io
import numpy as np
import random as rd
import os
import csv
import sys
from datetime import datetime
import matplotlib.pyplot as plt

from size_distribution import plot

def create_image_array(xsize, ysize):
    array = np.zeros((xsize, ysize), dtype=np.uint8)
    return array

def draw_background(array,pix_val_av,pix_val_noise):
    size = array.shape
    xsize = size[0]
    ysize = size[1]
    for i in range(xsize):
        for j in range(ysize):
            array[i,j] = pix_val_av + rd.randint(-pix_val_noise,pix_val_noise)
    return array

def draw_particle(array,xsize,ysize,pcx,pcy,pr,pix_val_av,pix_val_noise):
    for i in range (xsize):
        for j in range(ysize):
            rsq = (i-pcx)**2 + (j-pcy)**2
            if rsq < pr**2:
                array[i,j] = pix_val_av + rd.randint(-pix_val_noise,pix_val_noise)
    return array

def create_first_particle(array,rad_min,rad_max,pix_val_av,pix_val_noise, particle_list):
    size  = array.shape
    xsize = size[0]
    ysize = size[1]
    xtemp = rd.randint(1,xsize)
    ytemp = rd.randint(1,ysize)
    rtemp = rd.randint(rad_min,rad_max)
    particle_list.append([xtemp,ytemp,rtemp])
    array_new = draw_particle(array,xsize,ysize,xtemp,ytemp,rtemp,pix_val_av,pix_val_noise)
    return array_new, particle_list

def add_more_particles(array,rad_min,rad_max,pix_val_av,pix_val_noise,particle_number,radius_overlap, fname, particle_list):
    size  = array.shape
    xsize = size[0]
    ysize = size[1]

    for k in range(particle_number):
        overlap_flag = 0

        xtemp = rd.randint(1,xsize)
        ytemp = rd.randint(1,ysize)
        rtemp = rd.randint(rad_min,rad_max)

        for m in range(len(particle_list)):
            min_dist_sq = (1.0 - radius_overlap)*(rtemp + particle_list[m][2])**2
            distsq = (xtemp-particle_list[m][0])**2 + (ytemp-particle_list[m][1])**2
            if distsq <= min_dist_sq:
                overlap_flag = 1

        if overlap_flag == 1:
            continue
        
        particle_list.append([xtemp,ytemp,rtemp])
        array_new = draw_particle(array,xsize,ysize,xtemp,ytemp,rtemp,pix_val_av,pix_val_noise)

        with open(fname, "a") as f:
            writer = csv.writer(f)
            writer.writerow((rtemp,))

    return array_new, particle_list

# run main program calling previously defined functions
def main(number):
    # Filename
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y_%H.%M.%S")
    fname = "sizes_" + timestampStr + ".csv"

    if not os.path.exists('./Out'):
        os.makedirs('./Out')
    
    for i in range(number):
        particle_list = []
        print(f"Itteration: {i}")

        image_array = create_image_array(512, 512)

        # image_array = draw_background(array created above, average pixel value, noise level)
        image_array = draw_background(image_array, 100, 25)
        
        # image_array = create_first_particle(background array, min radius, max radius, average pixel value, noise level)
        try:
            image_array, particle_list = create_first_particle(image_array, 20, 40, 200, 25, particle_list)
        except: continue

        #image_array = add_more_particles(array with 1 particle, min radius, max radius, average pixel value, noise level, number of insertion trials, allowed radius overlap, fname)
        try:
            image_array, particle_list = add_more_particles(image_array, 20, 40, 200, 25, 100, 0.05, fname, particle_list)
        except: continue

        # Save image
        filename = "./Out/particles" + str(i) + ".tif"
        try:
            io.imwrite(filename, image_array)
        except:
            raise Exception(f"Could not write particles{i}.png to './Out/particles/'")

    plot(fname)

if __name__== "__main__" :
    try:
        number = int(sys.argv[1])
    except: 
        print(f"\nUsage: python3 {os.path.basename(__file__)} [number of images/masks to generate]\n")
        sys.exit(1)

    main(number)