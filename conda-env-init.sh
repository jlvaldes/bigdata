#!/bin/bash
# conda create -n big-data python=3.10

# bash -i conda-env-init.sh   
conda install -c conda-force python=3.10
conda install -c conda-forge pandas
conda install -c conda-forge prefect
conda install -c conda-force ipykernel
conda install -c conda-force sqlalchemyconda activate 
conda install sqlalchemy
pip install psycopg2-binary
pip install numpy
pip install nltk
pip install scikit-learn