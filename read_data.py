import glob, os
import pandas as pd
import numpy as np

GENRE_POS = 2

def read_all_data():    
    data_location = r'Data'
    all_data = glob.glob( os.path.join(data_location, "datos_abiertos_*.csv") )

    df_from_each_file = (pd.read_csv(f, low_memory = False) for f in all_data)
    concatenated_df = pd.concat(df_from_each_file)
    concatenated_df.Genero = concatenated_df.Genero.map(lambda g: 1 if g == 'H' else -1)

    return concatenated_df.dropna(how='any')

def read_sample_data():    
    
    df = pd.read_csv("Data/datos_abiertos_2017_01.csv",  low_memory = False)
    df.Genero = df.Genero.map(lambda g: 1 if g == 'H' else -1)
    #print(df.Genero.sum())
    return df.dropna(how='any')

def nomenclatura():
    """ Return a dictionary with the latitude and longitude of each bike station """
    df = pd.read_csv("Data/nomenclatura_1.csv", encoding = "latin1")
    #dict_axis = df.set_index('id').T.to_dict('list')
    dict_axis = dict( [ (i, [a,b]) for i, a,b in zip(df.id, df.latitude, df.longitude) ] )

    return dict_axis


def print_data():
    data = read_sample_data()
    print(data)

#print_data()

#dict_node = dict( zip( df["id"], df["label"] ) )
#departures_list = data['Origen_Id'].values.tolist()