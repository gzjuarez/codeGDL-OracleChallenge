import pandas as pd
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np

import read_data

def calculate_intervals(max, min, size):
    rang = max - min
    k = 1 + np.log2(size)
    return rang / k

data = read_data.read_sample_data()

birth_year = data['Ano_de_nacimiento']
birth_year = birth_year.filter(regex='^\d{4}$')
birth_year = birth_year.astype('int64')

data['Ano_de_nacimiento'] = birth_year

intervals = calculate_intervals(birth_year.max(), birth_year.min(), birth_year.size)
#print(pd.cut(birth_year, intervals))

#grouped = data.groupby(pd.cut(birth_year, np.arange(birth_year.min(), birth_year.max(), 4)))
grouped = data.groupby(['Ano_de_nacimiento', 'Genero']).agg('count')['Viaje_Id']

print(grouped)
#grouped.plot()
#plt.show()

#grouped = data.groupby(pd.cut(data['Ano_de_nacimiento'], 10))
#print(pd.cut(birth_year.astype('int64'), 50))
#print(birth_year)

#for name, group in grouped:
#    print (name)
#    print (group)

#for index, row in data.iterrows():
#    print(row['Ano_de_nacimiento'])