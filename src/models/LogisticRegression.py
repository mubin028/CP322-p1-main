import numpy as np

class LR:

    def fit(self, X, Y, learningRate, iterations):
        self.trainingData = X
        self.target = Y
        self.learningRate = learningRate
        self.iterations = iterations
        self.w = np.zeros(X.shape[1])
        self.b = 0
        self.gradientDecent()
    
    def predict(self, X):
        prediction = []
        for x in X:
            if self.f(x) >= 0.5:
                prediction.append(1)
            else:
                prediction.append(0)
        return prediction

    def sigmoidFunction(self, z):
        return 1 / (1 + np.exp(-z))

    def f(self, X):
        z = np.dot(self.w, X) + self.b
        return self.sigmoidFunction(z)

    def costFunction(self):
        m = len(self.target)
        costSum = 0
        for i in range(m):
            costSum +=  (self.target[i] * np.log(self.f(self.trainingData[i]))
                          + (1 - self.target[i]) * np.log(1 - self.f(self.trainingData[i])))
        return costSum * (-1/m)
    
    def gradientDecent(self):
        threshold = 0.001
        m = len(self.trainingData)
        cost = 1
        lastCost = 0
        for _ in range(self.iterations):
            if abs(cost - lastCost) < threshold:
                return
            lastCost = cost
            for i in range(m):
                temp_w = self.w - self.learningRate * ((1/m) * (self.f(self.trainingData[i]) - self.target[i]) * self.trainingData[i])
                temp_b = self.b - self.learningRate * ((1/m) * (self.f(self.trainingData[i]) - self.target[i]))
                self.w = temp_w
                self.b = temp_b
            cost = self.costFunction()

def evaluate_acc(Y, predictions):
    length = len(predictions)
    correct = 0
    for i in range(length):
        if predictions[i] == Y[i]:
            correct += 1
    return correct/length


