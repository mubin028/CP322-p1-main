
import np_import as util_np
import numpy as np

class KNNModel:
    def __init__(self, k=5):
        self.k = k
    
    # Fits the training parameters to the model
    def fit(self, x, y):
        self.training_data = x
        self.target = y
    
    # Predicts the targets for the provided data
    def predict(self, new_data):
        result = np.empty(len(new_data))
        for i, new_entry in enumerate(new_data):
            distances = np.linalg.norm(new_entry - self.training_data, axis=1)
            index_values = np.argsort(distances)
            index_values = index_values[:self.k]
            nearest = self.target[index_values]
            result[i] = self._majority_class(nearest)
            
        return result
    
    # Helper function for predict(), finds the majority class among an array
    def _majority_class(self, neighbours):
        count = {}
        for entry in neighbours:
            if entry not in count:
                count[entry] = 0
            count[entry] += 1
        return max(count, key=count.get)
    

# Given true_labels and prediction (predicted labels), finds the accuracy of the prediction
def evaluate_acc(true_labels, prediction):
    correct = np.sum(true_labels == prediction)
    total = len(prediction)
    return correct / total

