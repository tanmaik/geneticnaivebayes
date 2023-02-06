import numpy as np
from tqdm import tqdm 
from sklearn.model_selection import train_test_split
import sys


def naive_accuracy(weights):
    X = np.loadtxt(open("final_dataset_genetic.csv", "rb"), delimiter=",", usecols=range(14), skiprows=1, dtype=int)
    y = np.loadtxt(open("final_dataset_genetic.csv", "rb"), delimiter=",", usecols=range(14,15), skiprows=1, dtype=int)

    Xd_train, Xd_test, y_train, y_test = train_test_split(X, y, random_state = 0, stratify = y, test_size=0.3)


    num_observations = dict()

    for num in set(y):
        num_observations[num] = list(y_train).count(num)


    # print(f"\n# in each class value bucket: {num_observations}")
    training_num_observations = sum(num_observations.values())
    # print(f"# of total instances in the training set: {training_num_observations}\n")
    probabilities = dict()


    # print("Training...")
    # print("Calculating all probabilities to use during testing...")

    for num in set(y): # num = equal a class value 
        probabilities[num] = dict() # establishes a dictionary for each class value 
        for i in range(len(X[0])): # now looping through each of the attribute / features 
            probabilities[num][i] = dict() # establishes a dictionary for each attribute
            for j in range(training_num_observations): # now looping through each of the observations
                if y_train[j] == num: # if the observation has the same class value
                    if Xd_train[j][i] not in probabilities[num][i]: # let's check if the attribute value is in the dictionary
                        probabilities[num][i][Xd_train[j][i]] = 0 # if not, let's add it and set it to 0
                    probabilities[num][i][Xd_train[j][i]] += 1 # now we increment the value of the attribute by 1
            for value in range(6): 
                if value not in probabilities[num][i]: # if the attribute value is not in the dictionary
                    probabilities[num][i][value] = 0 # let's add it and set it to 0
            probabilities[num][i] = {k: v / num_observations[num] for k, v in probabilities[num][i].items()} # now we divide the value of the attribute by the number of observations of that class value


    # print("Probabilities calculated!\n")


    # print(f"\n# of test observations: {len(Xd_test)}")
    # print("Testing...\n")

    correct = 0
    total = 0
    confusion_matrix = np.zeros((len(set(y)), len(set(y))), dtype=int)
    for i in range(len(Xd_test)):
        testing_now = Xd_test[i]
        probs = []
        for num in set(y):
            accumulator = 1
            for attribute_value in range(len(testing_now)):
                accumulator = accumulator * (probabilities[num][attribute_value][testing_now[attribute_value]]**weights[attribute_value])
            accumulator = accumulator * (num_observations[num] / training_num_observations)
            probs.append(accumulator)
        prediction = probs.index(max(probs))
        if prediction == y_test[i]:
            correct += 1
        total += 1
        confusion_matrix[y_test[i],prediction] = confusion_matrix[y_test[i],prediction] + 1
        # print("i:", i, "Prediction: ", prediction, "Actual: ", y_test[i], "Correct: ", prediction == y_test[i])

    # print("\nTesting accuracy", correct/total * 100, "%")
    return correct/total * 100




def naive_confusion(weights):
    X = np.loadtxt(open("final_dataset_genetic.csv", "rb"), delimiter=",", usecols=range(14), skiprows=1, dtype=int)
    y = np.loadtxt(open("final_dataset_genetic.csv", "rb"), delimiter=",", usecols=range(14,15), skiprows=1, dtype=int)

    Xd_train, Xd_test, y_train, y_test = train_test_split(X, y, random_state = 0, stratify = y, test_size=0.3)


    num_observations = dict()

    for num in set(y):
        num_observations[num] = list(y_train).count(num)


    # print(f"\n# in each class value bucket: {num_observations}")
    training_num_observations = sum(num_observations.values())
    # print(f"# of total instances in the training set: {training_num_observations}\n")
    probabilities = dict()


    # print("Training...")
    # print("Calculating all probabilities to use during testing...")

    for num in set(y): # num = equal a class value 
        probabilities[num] = dict() # establishes a dictionary for each class value 
        for i in range(len(X[0])): # now looping through each of the attribute / features 
            probabilities[num][i] = dict() # establishes a dictionary for each attribute
            for j in range(training_num_observations): # now looping through each of the observations
                if y_train[j] == num: # if the observation has the same class value
                    if Xd_train[j][i] not in probabilities[num][i]: # let's check if the attribute value is in the dictionary
                        probabilities[num][i][Xd_train[j][i]] = 0 # if not, let's add it and set it to 0
                    probabilities[num][i][Xd_train[j][i]] += 1 # now we increment the value of the attribute by 1
            for value in range(6): 
                if value not in probabilities[num][i]: # if the attribute value is not in the dictionary
                    probabilities[num][i][value] = 0 # let's add it and set it to 0
            probabilities[num][i] = {k: v / num_observations[num] for k, v in probabilities[num][i].items()} # now we divide the value of the attribute by the number of observations of that class value


    # print("Probabilities calculated!\n")


    # print(f"\n# of test observations: {len(Xd_test)}")
    # print("Testing...\n")

    correct = 0
    total = 0
    confusion_matrix = np.zeros((len(set(y)), len(set(y))), dtype=int)
    for i in range(len(Xd_test)):
        testing_now = Xd_test[i]
        probs = []
        for num in set(y):
            accumulator = 1
            for attribute_value in range(len(testing_now)):
                accumulator = accumulator * (probabilities[num][attribute_value][testing_now[attribute_value]]**weights[attribute_value])
            accumulator = accumulator * (num_observations[num] / training_num_observations)
            probs.append(accumulator)
        prediction = probs.index(max(probs))
        if prediction == y_test[i]:
            correct += 1
        total += 1
        confusion_matrix[y_test[i],prediction] = confusion_matrix[y_test[i],prediction] + 1
        # print("i:", i, "Prediction: ", prediction, "Actual: ", y_test[i], "Correct: ", prediction == y_test[i])

    # print("\nTesting accuracy", correct/total * 100, "%")
    return confusion_matrix

