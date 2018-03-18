import glob, os
import pandas as pd
import numpy as np

def read_data():    
    data_location = r'Data'
    all_data = glob.glob( os.path.join(data_location, "datos_abiertos_*.csv") )

    df_from_each_file = (pd.read_csv(f, low_memory = False) for f in all_data)
    concatenated_df = pd.concat(df_from_each_file)

    return concatenated_df
    #df = pd.read_csv(data_location, low_memory = False)
    #print(concatenated_df.size)