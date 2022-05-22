from locale import D_FMT
import numpy as np
import pandas as pd
from os import path
from PIL import Image
import matplotlib.pyplot as plt

spoke_persons = ['dronning_2020','dronning_2019','statsminister_2020','statsminister_2019']
files_to_read = ['d_tale_2020.csv','d_tale_2019.csv','s_tale_2020.csv','s_tale_2019.csv']

#function to fetch all of our speeches from csv files
def fetch_speeches():
    data = {}
    for i, c in enumerate(spoke_persons):
        with open(files_to_read[i]) as file:
            data[c] = file.read()
    return data       
dct_of_speeches = fetch_speeches()

#function to change value format into string.
def combine_text(lst_of_text):
    combined_text = ''.join(lst_of_text)
    return combined_text

data_combined = {key: [combine_text(value)] for (key, value) in dct_of_speeches.items()}

#change to pandas dataframe
data_df = pd.DataFrame.from_dict(data_combined).transpose()
data_df.columns = ['speeches']
data_df = data_df.sort_index()

#print(data_df.speeches.loc['dronning_2020'])