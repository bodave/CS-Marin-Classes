#-------------------------------------------------------------------------
# AUTHOR: David Bohon
# FILENAME: naive_bayes.py
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

#reading the training data in a csv file
#--> add your Python code here
dbTraining = []
featuresNums= {"Sunny": 1, "Hot": 1, "High": 1, "Strong": 1,
                       "Overcast": 2, "Mild": 2, "Normal": 2, "Weak": 2,
                       "Rain": 3, "Cool": 3}
classesNums = {"Yes": 1,
                      "No": 2}

with open("weather_training.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:
            dbTraining.append(row)
#transform the original training features to numbers and add them to the 4D array X.
#For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
# X =
X = []
for item in dbTraining:
    features = [featuresNums[item[1]], featuresNums[item[2]], featuresNums[item[3]], featuresNums[item[4]]]
    X.append(features)
    
#transform the original training classes to numbers and add them to the vector Y.
#For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
# Y =
Y = []
for item in dbTraining:
    Y.append(classesNums[item[5]])

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the test data in a csv file
#--> add your Python code here
dbTest = []
dbHeader = []
with open("weather_test.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:
            dbTest.append(row)
        else:
            dbHeader.append(row)
            
X1 = []
for item in dbTest:
    temp = []
    for j in range(len(item)):
        if j == 0:
            continue
        elif j >= len(item) - 1:
            continue

        temp.append(featuresNums[item[j]])

    X1.append(temp)
#printing the header os the solution
#--> add your Python code here
for i in range(len(dbHeader[0])):
    print(dbHeader[0][i].ljust(15), end = "")

print()
#use your test samples to make probabilistic predictions. For instance: clf.predict_proba([[3, 1, 2, 1]])[0]
#--> add your Python code here
for i in range(len(dbTest)):
    yesCount, noCount = clf.predict_proba([X1[i]])[0]
    if yesCount >= 0.75:
        for j in range(len(dbTest[i]) - 1):
            print(dbTest[i][j].ljust(15), end = "")
        print(f"Yes: Confidence- {yesCount}".ljust(15), end = "")
        print()
    elif noCount >= 0.75:
        for j in range(len(dbTest[i]) - 1): 
            print(dbTest[i][j].ljust(15), end = "")
        print(f"No: Confidence-  {noCount}".ljust(15), end = "")
        print()

