import numpy as np
import random
import math as math
import statistics as stat

data = np.loadtxt(fname='F:\Code\k-nn\ABiris.data', dtype = 'str', delimiter = ",")
print(data)
def create_point():
    point = []
    for _ in range(4):
        point.append(round(random.random() * 10, 1))
    return point

point1 = create_point()

print(point1)
data_del = np.delete(data, 0, 0)
data_shape = data_del.shape

def counting_distance(point, data_shape, data):
    distances = []
    count = []
    for i in range(data_shape[0]):
        for j in range(data_shape[1]-1):
            count.append((float(point[j]) - float(data[i][j]))**2)
        distances.append([math.sqrt(sum(count)), data[i][(data_shape[1]-1)]])
        count = []
        distances.sort()
    return distances

all_distances = counting_distance(point1, data_shape, data_del)
print(all_distances)
def choosing_class(distances):
    common = []
    for i in range(7):
        common.append(distances[i][1])
    return stat.mode(common)

point_class = choosing_class(all_distances)

print("point class is", point_class)
