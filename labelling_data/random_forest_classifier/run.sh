 #!/bin/sh

#$ -cwd
#$ -N TEM_training_v1
#$ -m be

python3 training_using_feature_extraction_and_random_forest.py
