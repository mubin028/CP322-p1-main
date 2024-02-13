import numpy as np
import csv

# headers = ["buy_price", "Maint_price", "door_count", "person_count", "trunk_space", "safety_measure", "eval_class"]

# print the headers
# for i in range(len(headers)):
#     print(headers[i], end="")
#     if i != (len(headers)-1):
#         print(',', end="")

# dictionaries
price_dict = {'vhigh': 3, 'high': 2, 'med': 1, 'low': 0}
door_dict = {'2': 0, '3': 1, '4': 2, '5more': 3}
person_dict = {'2': 0, '4': 1, 'more': 2}
trunk_dict = {'small': 0, 'med': 1, 'big': 2}
safety_dict = {'low': 0, 'med': 1, 'high': 2}
eval_dict = {'unacc': 0, 'acc': 1, 'good': 2, 'vgood': 3}

filedata = np.loadtxt("data/car.data", dtype='str', delimiter=",")
temp = filedata.T

# one hot encoding
for i,j in price_dict.items():
    for x in range(len(temp[0])):
        if i == temp[0][x]:
            temp[0][x] = j
    for y in range(len(temp[1])):
        if i == temp[1][y]:
            temp[1][y] = j

for i,j in door_dict.items():
    for x in range(len(temp[2])):
        if i == temp[2][x]:
            temp[2][x] = j

for i,j in person_dict.items():
    for x in range(len(temp[3])):
        if i == temp[3][x]:
            temp[3][x] = j

for i,j in trunk_dict.items():
    for x in range(len(temp[4])):
        if i == temp[4][x]:
            temp[4][x] = j

for i,j in safety_dict.items():
    for x in range(len(temp[5])):
        if i == temp[5][x]:
            temp[5][x] = j

for i,j in eval_dict.items():
    for x in range(len(temp[6])):
        if i == temp[6][x]:
            temp[6][x] = j

# filedata = filedata.astype(int)

with open("data/car_clean.data", "w") as f:
    for x in filedata:
        for i in range(len(x)):
            print(x[i], end="")
            f.write(x[i])
            if i != (len(x)-1):
                print(',', end="")
                f.write(',')
        print("\n")
        f.write("\n")

# statistics
# print(np.peicentile(filedata[0], 75))