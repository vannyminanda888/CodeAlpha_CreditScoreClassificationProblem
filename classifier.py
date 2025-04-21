#installing some libs
import subprocess
import sys

# List your required packages
required_packages = ['pandas', 'numpy', 'scikit-learn']

for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

#importing some libs
import pandas as pd
import numpy as np

#read dataset:
data = pd.read_csv("Credit Score Classification Dataset.csv")
data.head()

#Dana Analysis
data.shape()
