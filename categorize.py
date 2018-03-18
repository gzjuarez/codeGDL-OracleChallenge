import read_data

station = {
    "inicios": 0,
    "destinos": 0,
    "nacimiento": 0,
    "tiempo_llegada": 0,
    "tiempo_salida": 0,
    "genero": 0,
    "tiempo_inicio": 0
}

print(read_data.read_data()["Destino_Id"][9])
