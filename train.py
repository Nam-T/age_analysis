import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the data, converters convert the letter to a number
data= np.loadtxt('data.txt', dtype= 'float32', delimiter = ',')
data_test= np.loadtxt('data_test.txt', dtype= 'float32', delimiter = ',')

# split the data to two, 10000 each for train and test
#train, test = np.vsplit(data,2)

# split trainData and testData to features and responses
responses, trainData = np.hsplit(data,[1])
#labels, testData = np.hsplit(test,[1])

# Initiate the kNN, classify, measure accuracy.
knn = cv2.ml.KNearest_create()
knn.train(trainData, 0, responses)
ret, result, neighbours, dist = knn.findNearest(data_test, k=12)

print(result)
#correct = np.count_nonzero(result == labels)
#accuracy = correct*100.0/10000
#print(accuracy)

f = open("agedetector_group_test_unlabel.v1.0.txt", "r")
file_data_test = open("agedetector_group_test.v1.0.txt", "w")

LABEL_HASH = {
            0: '__label__18-24',
            1: '__label__55+',
            2: '__label__45-54',
            3: '__label__25-34',
            4: '__label__35-44'
        }

result_arr = np.array(result)
print(result_arr[1])
i = 0
for x in f:
    arr = x.strip('\n').split(' ')
    label = LABEL_HASH[result_arr[i][0]]
    file_data_test.write(label + ' ')
    j = 1
    for data in arr:
        if j < len(arr):
            file_data_test.write(data + ' ')
        else:
            file_data_test.write(data)
        j += 1
    file_data_test.write('\n')

    i += 1
file_data_test.close()