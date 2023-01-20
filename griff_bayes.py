from scipy.io import arff
import sys
import numpy as np


df = np.loadtxt(open("credit_approved_headings_weka.csv", "rb"), delimiter=",", usecols=range(14), skiprows=1, dtype=int) 
df2 = pd.DataFrame(data[0])

def display_confusion(confusion):
   print('Order: ', end = '')
   for x in confusion:
      print(x, end = ' ')
   print()
   for x in confusion:
      print(confusion[x])

def conditionalProb(df,attribute,class_label,attribute_label):
    numerator = 0
    denominator = 0
    for x in range(len(df)):
        if df[df.keys()[-1]][x] == class_label:
            denominator += 1
            if df[attribute][x] == attribute_label:
                numerator += 1
    if denominator == 0:
        return 0.0
    return numerator/denominator

def create_instance(df,z):
    instance = []
    for x in df.keys():
        if not x == df.keys()[-1]:
            instance.append(df[x][z])
    return instance

def calc_prob(probs,instance,class_label,class_prob):
    prob = class_prob/len(df)
    for x in instance:
        prob = prob*probs[x][class_label]
    return prob

def class_probs(classes,df):
    thingy = {}
    for x in range(len(df)):
        if df[df.keys()[-1]][x] not in thingy:
            thingy[df[df.keys()[-1]][x]] = 1
        else:
            thingy[df[df.keys()[-1]][x]] = thingy[df[df.keys()[-1]][x]]+1
    return thingy
def naive_bayes():
    classes = []
    for x in range(len(df)):
        classes.append(df[df.keys()[-1]][x])
    classes = set(classes)
    classes = list(classes)
    class_dist = class_probs(classes,df)
    probs = {}
    holder = []
    class_number = {}
    for x in range(len(classes)):
        class_number[classes[x]] = x
        holder.append(0)
    for x in range(len(df)):
        for y in df.keys():
            if not df[y][x] == df[df.keys()[-1]][x]:
                if df[y][x] not in probs:
                    probs[df[y][x]] = holder[:]
                if probs[df[y][x]][class_number[df[df.keys()[-1]][x]]] == 0:
                    probs[df[y][x]][class_number[df[df.keys()[-1]][x]]] = conditionalProb(df,y,df[df.keys()[-1]][x],df[y][x])
    correct = 0
    holder = []
    confusion = {}
    for x in range(len(classes)):
        holder.append(0)
    for x in classes:
        confusion[x] = holder[:]
    for x in range(len(df2)):
        max = 0
        classification = 0
        instance = create_instance(df2,x)
        for y in range(len(classes)):
            probability = calc_prob(probs,instance,y,class_dist[classes[y]])
            print(classes[y], end = ':  ')
            print(probability)
            if probability > max:
                max = probability
                classification = y
        print(classes[classification])
        print()
        print()
        print()
        confusion[df2[df2.keys()[-1]][x]][class_number[classes[classification]]] += 1
        if classes[classification] == df2[df2.keys()[-1]][x]:
            correct += 1
    print("NaiveBayes Accuracy: " + str(correct/len(df2)*100) + '%')
    display_confusion(confusion)
    print()


def main():
    naive_bayes()

if __name__ == '__main__': main()