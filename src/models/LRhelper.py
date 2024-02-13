import LogisticRegression
import numpy as np
import np_import
import matplotlib.pyplot as plt

def readFile(file):
    data = np_import.generate_np_array(file)
    np_import.normalize_data(data)
    return data

def getValues(data):
    X = data[:, :-1]
    Y = data[:, -1]
    return X, Y

def getAccuracy(LR, X, Y, learningRates, iterations):
    foldSize = len(X) // 5
    total_accuracy = []
    for rate in learningRates:
        fold_accuracy = []
        for i in range(5):
            start = i * foldSize
            end = (i + 1) * foldSize
            trainingX = np.concatenate([X[:start], X[end:]])
            trainingY = np.concatenate([Y[:start], Y[end:]])
            LR.fit(trainingX, trainingY, rate, iterations)
            testingX = X[start:end]
            testingY = Y[start:end]
            prediction = LR.predict(testingX)
            fold_accuracy.append(LogisticRegression.evaluate_acc(testingY, prediction))
        total_accuracy.append(sum(fold_accuracy)/5)
    return total_accuracy

def plotGraph(X, Y):
    plt.plot(X, Y, marker='o')
    plt.xlabel('Learning Rate')
    plt.ylabel('Accuracy')
    plt.grid(True)
    plt.show()
