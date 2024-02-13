

import numpy as np

# Returns 2D numpy array
def generate_np_array(file_path):
    header_val = 0
    # Ignores header if file is .csv
    if ".csv" in file_path:
        header_val = 1
    data = np.genfromtxt(file_path, delimiter=",", skip_header=header_val)
    np.random.shuffle(data)
    return data

# Min-max normalization
def normalize_data(data):
    for i in range(data[0].size):
        data_min = np.min(data[:, i])
        data_max = np.max(data[:, i])
        data[:, i] = (data[:, i] - data_min) / (data_max - data_min)