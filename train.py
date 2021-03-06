import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the data, converters convert the letter to a number
data= np.loadtxt('data.txt', dtype= 'float32', delimiter = ',')

# split the data to two, 10000 each for train and test
train, test = np.vsplit(data,2)

# split trainData and testData to features and responses
responses, trainData = np.hsplit(train,[1])
labels, testData = np.hsplit(test,[1])

# Initiate the kNN, classify, measure accuracy.
knn = cv2.ml.KNearest_create()
knn.train(trainData, 0, responses)

ret, result, neighbours, dist = knn.findNearest(testData, k=5)

#print(testData[1])
correct = np.count_nonzero(result == labels)
accuracy = correct*100.0/10000
print(accuracy)