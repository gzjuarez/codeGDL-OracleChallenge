import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sklearn.cluster import KMeans
import math

import read_data

def calculate_intervals(max, min, size):
    rang = max - min
    k = 1 + np.log2(size)
    return rang / k

data = read_data.read_sample_data()

#print(pd.cut(birth_year, intervals))
#data_filtered_birth = data[ len(data['Ano_de_nacimiento'].str) == 4]
data['Ano_de_nacimiento'] = data['Ano_de_nacimiento'].astype(str)
data_filtered_birth = data.filter(regex='^\d{4}$', axis=0)

list_genre = data_filtered_birth['Genero'].values.tolist()
list_estacion_origen = data_filtered_birth['Origen_Id'].values.tolist()
list_nacimiento = data['Ano_de_nacimiento'].filter(regex='^\d{4}$').astype('float64').values.tolist()
list_nacimiento = list(map(lambda n: math.floor((2017 - n) / 10) * 10, list_nacimiento))

list_k = []

genre_av = np.mean(np.array(list_genre))
origen_av = np.mean(np.array(list_estacion_origen))
nacimiento_av = np.mean(np.array(list_nacimiento))

genre_sdev = np.std(np.array(list_genre))
origen_sdev = np.std(np.array(list_estacion_origen))
nacimiento_sdev = np.std(np.array(list_nacimiento))

print(
    genre_av,
    genre_sdev,
    origen_av,
    origen_sdev,
    nacimiento_av,
    nacimiento_sdev
)

for i in range(len(list_nacimiento)):
    tup = ((list_genre[i] - genre_av) / genre_sdev,
           (list_estacion_origen[i] - origen_av) / origen_sdev,
           (list_nacimiento[i] - nacimiento_av) / origen_sdev
    )
    list_k.append(tup)

colors =  np.array(['k', 'r', 'b', 'g', 'y', 'c', 'm', 'lime', 'hotpink', 'teal'])
markers = np.array(['x', 'o', '^', '*', 'h', 's', 'D', 'P', '8', '4'])
X = np.array(list_k)
kmeans = KMeans(n_clusters=5, random_state=1).fit(X)

plt.plot(list_estacion_origen[list_genre == -1], list_nacimiento[list_genre == -1])
plt.plot(list_estacion_origen[list_genre == 1], list_nacimiento[list_genre == 1])
plt.show()

input()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i, coords in enumerate(kmeans.cluster_centers_):
    ax.scatter(coords[0], coords[1], coords[2], c=colors[i%10], marker='X')

for x, y, z, label in zip(list_genre, list_estacion_origen, list_nacimiento, kmeans.labels_):
    ax.scatter(x, y, z, c=colors[label], marker=markers[label])

ax.set_xlabel('Genero')
ax.set_ylabel('Estacion')
ax.set_zlabel('Nacimiento')

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
