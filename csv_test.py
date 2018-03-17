import pandas as pd
from datetime import datetime
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

big_data = pd.read_csv('Data/datos_abiertos_2017_01.csv')

# set weekday and convert
big_data['Inicio_del_viaje'] = big_data['Inicio_del_viaje'].map(lambda date_str: datetime.strptime(date_str, '%d/%m/%Y %H:%M'))
big_data['Fin_del_viaje'] = big_data['Fin_del_viaje'].map(lambda date_str: datetime.strptime(date_str, '%d/%m/%Y %H:%M'))
big_data['dia_semana'] = big_data['Inicio_del_viaje'].map(lambda date: date.weekday())
big_data['hour'] = big_data.Inicio_del_viaje.map(lambda date: date.hour)

for x in range(7):
    n, bins, _ = plt.hist(big_data.loc[(big_data.dia_semana == x), 'hour'], bins=24, histtype='step')
plt.show()

print (big_data)
