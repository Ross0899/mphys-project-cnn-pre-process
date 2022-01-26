#!/bin/sh

#$ -cwd
#$ -N model_v3_predicting_training_data_areas
#$ -m be

python3 predicted_size_distribution.py
