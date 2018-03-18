import read_data
import matplotlib.pyplot as plt

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

def plot_matrix():
    matrix = make_matrix(read_data.read_all_data())
    stations = read_data.nomenclatura()
    # stations = {
    #     3: allstations[3],
    #     4: allstations[4],
    #     5: allstations[5],
    #     6: allstations[6],
    #     100: allstations[100],
    # }
    max_val = max([max(row) for row in matrix])
    for k1, i in stations.items():
        for k2, j in stations.items():
            val = matrix[k1][k2]
            if val / max_val > 0.2:
                col = (1.0 - (val / max_val), 1.0 - (val / max_val), 1.0 - (val / max_val))
                plt.plot([i[0], j[0]], [i[1], j[1]], color = col)
                # print(k1, k2, val, col)
        print(k1)
    plt.show()

plot_matrix()
# print(make_matrix(read_data.read_all_data()))
