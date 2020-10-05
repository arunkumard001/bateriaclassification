#preprocessing
import os
import csv
import numpy as np
import scipy.io as sc

def create_dataset(int IMG_SIZE = 128,DATA_DIR="data/"):
    output_file="data/dataset.mat"