import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sklearn.cluster import KMeans
import math
from datetime import datetime

import read_data

data = read_data.read_all_data()

#print(pd.cut(birth_year, intervals))
#data_filtered_birth = data[ len(data['Ano_de_nacimiento'].str) == 4]
data['Ano_de_nacimiento'] = data['Ano_de_nacimiento'].astype(str)
data_filtered_birth = data.filter(regex='^\d{4}$', axis=0)

list_genre = data_filtered_birth['Genero'].values.tolist()
list_estacion_origen = data_filtered_birth['Origen_Id'].values.tolist()
list_estacion_destino = data_filtered_birth['Destino_Id'].values.tolist()
list_nacimiento = data['Ano_de_nacimiento'].filter(regex='^\d{4}$').astype('float64').values.tolist()
list_nacimiento = list(map(lambda n: math.floor((2017 - n) / 10) * 10, list_nacimiento))
list_month = data['Inicio_del_viaje'].map(lambda date_str: datetime.strptime(date_str, '%d/%m/%Y %H:%M') if '/' in date_str else datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')).map(lambda date: date.month)

list_k = [[0, 0] for i in range(254)]

genre_av = np.mean(np.array(list_genre))
origen_av = np.mean(np.array(list_estacion_origen))
nacimiento_av = np.mean(np.array(list_nacimiento))

genre_sdev = np.std(np.array(list_genre))
origen_sdev = np.std(np.array(list_estacion_origen))
nacimiento_sdev = np.std(np.array(list_nacimiento))

for i in range(len(list_nacimiento)):
    list_k[list_estacion_origen[i]][0] += 1
    list_k[list_estacion_destino[i]][1] += 1

colors =  np.array(['k', 'r', 'b', 'g', 'y', 'c', 'm', 'lime', 'hotpink', 'teal'])
markers = np.array(['x', 'o', '^', '*', 'h', 's', 'D', 'P', '8', '4'])
X = np.array(list_k)
kmeans = KMeans(n_clusters=5, random_state=1).fit(X)

plt.plot(list_estacion_origen[list_genre == -1], list_nacimiento[list_genre == -1])
plt.plot(list_estacion_origen[list_genre == 1], list_nacimiento[list_genre == 1])
plt.show()

input()

fig = plt.figure()
ax = fig.add_subplot(111)
# for i, coords in enumerate(kmeans.cluster_centers_):
#     ax.scatter(coords[0], coords[1], coords[2], c=colors[i%10], marker='X')

for visits, label in zip(list_k, kmeans.labels_):
    print(visits, label)
    ax.scatter(visits[0], visits[1], c=colors[label], marker=markers[label])

ax.set_xlabel('Origenes')
ax.set_ylabel('Destinos')
# ax.set_zlabel('Nacimiento')

plt.show()

#data_filtered_birth['Ano_de_nacimiento'] = data_filtered_birth['Ano_de_nacimiento'].astype("float64")
# grouped = data_filtered_birth.groupby(['Origen_Id', 'Ano_de_nacimiento', 'Genero']).agg('count')['Viaje_Id']

#print(grouped)
#input()
#print(grouped.unstack())

#grouped = data.groupby(pd.cut(data['Ano_de_nacimiento'], 10))
#print(pd.cut(birth_year.astype('int64'), 50))
#print(birth_year)

#for name, group in grouped:
#    print (name)
#    print (group)

#for index, row in data.iterrows():
#    print(row['Ano_de_nacimiento'])
