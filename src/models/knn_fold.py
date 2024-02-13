

import np_import as util_np
import KNNModel as knn
import matplotlib.pyplot as plt
import numpy as np
import math

def knn_fold(file_path):
    data = util_np.generate_np_array(file_path)
    util_np.normalize_data(data)

    data_len = len(data)

    # Arbitrary maximum value for k (change if you want)
    max_k = round(math.sqrt(len(data)))

    # Arrays for plotting
    k_values = []
    final_acc = []

    for k in range(1, max_k):
        # fold_accuracy keeps track of accuracy of current k
        fold_accuracy = []

        # Iterate through 5 folds
        i = 0.0
        while i < 1.0:
            y_start = round(i * data_len)
            y_end = round((i + 0.2) * data_len)
            model = knn.KNNModel(k)

            # Fit data to model
            x = np.concatenate([data[0:y_start, :-1], data[y_end:data_len, :-1]])
            y = np.concatenate([data[0:y_start, -1], data[y_end:data_len, -1]])
            model.fit(x, y)

            # Data to be predicted
            new_data = data[y_start:y_end, :-1]
            true_labels = data[y_start:y_end, -1]

            prediction = model.predict(new_data)
            # Calculate accuracy, add to fold_accuracy for current k
            fold_accuracy.append(knn.evaluate_acc(true_labels, prediction))
            i += 0.2

        # Calculate average accuracy of k
        k_accuracy = sum(fold_accuracy) / len(fold_accuracy)

        k_values.append(k)
        final_acc.append(k_accuracy)

        print(f"{k} is finished!")
        print(f"k = {k}")
        print(f"accuracy = {k_accuracy}")

    return k_values, final_acc

k_values, final_acc = knn_fold("data/heart_disease_clean01.data")


plt.plot(k_values, final_acc)

plt.xlabel("k value")
plt.ylabel("Accuracy")

plt.xlim(1, len(k_values))
plt.ylim(min(final_acc)-0.1, 1)

plt.grid(True)
plt.show()
