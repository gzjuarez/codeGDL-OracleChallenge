import glob, os
import pandas as pd
import numpy as np

GENRE_POS = 2

def read_all_data():    
    data_location = r'Data'
    all_data = glob.glob( os.path.join(data_location, "datos_abiertos_*.csv") )

    df_from_each_file = (pd.read_csv(f, low_memory = False) for f in all_data)
    concatenated_df = pd.concat(df_from_each_file)

    return concatenated_df.dropna(how='any')

def read_sample_data():    
    
    df = pd.read_csv("Data/datos_abiertos_2017_01.csv",  low_memory = False)

    return df.dropna(how='any')

def print_data():
    data = read_sample_data()
    print(data)

#print_data()