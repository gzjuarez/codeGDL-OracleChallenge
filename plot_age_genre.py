import pandas as pd
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np

import read_data

def calculate_intervals(max, min, size):
    rang = max - min
    k = 1 + np.log2(size)
    return rang / k

data = read_data.read_all_data()

#print(pd.cut(birth_year, intervals))
#data_filtered_birth = data[ len(data['Ano_de_nacimiento'].str) == 4]

data_filtered_birth = data.set_index('Ano_de_nacimiento').filter(regex='^\d{4}$', axis=0)
grouped = data_filtered_birth.groupby(['Ano_de_nacimiento', 'Genero']).agg('count')['Viaje_Id']

print(grouped)

#grouped = data.groupby(pd.cut(data['Ano_de_nacimiento'], 10))
#print(pd.cut(birth_year.astype('int64'), 50))
#print(birth_year)

#for name, group in grouped:
#    print (name)
#    print (group)

#for index, row in data.iterrows():
#    print(row['Ano_de_nacimiento'])