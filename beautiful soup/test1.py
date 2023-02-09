import pandas as pd
from multiprocessing import process
import os

data = pd.read_csv('Weather_Data.csv')

print(data.head(15))