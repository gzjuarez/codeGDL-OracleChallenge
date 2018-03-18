import read_data

def make_matrix(data):
    matrix = [[0 for i in range(254)] for j in range(254)]
    arrivals_list = data['Destino_Id'].values.tolist()
    departures_list = data['Origen_Id'].values.tolist()

    #print (len(arrivals_list) * 8)
    #print (data.size)

    for i in range(len(arrivals_list)):
        #print(departures.take([i]))
        currentX = departures_list[i]
        currentY = arrivals_list[i]
        matrix[currentX][currentY] += 1

    return matrix

print(make_matrix(read_data.read_all_data()))
