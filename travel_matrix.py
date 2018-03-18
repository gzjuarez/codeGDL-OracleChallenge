import read_data

def make_matrix(data):
    matrix = [[0 for i in range(254)] for j in range(254)]
    arrivals = data['Destino_Id']
    departures = data['Origen_Id']
    for i in range(data.size):
        print(departures.take([i]))
        # matrix[departures[i]][arrivals[i]] += 1
    return matrix


print(make_matrix(read_data.read_data()))
