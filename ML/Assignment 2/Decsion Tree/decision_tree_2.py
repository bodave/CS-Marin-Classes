#-------------------------------------------------------------------------
# AUTHOR: David Bohon
# FILENAME: decision_tree_2.py
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)

    #transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
    # so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here
    # Mapping for feature transformation
    age_mapping = {'Young': 1, 'Presbyopic': 3, 'Prepresbyopic': 2}
    prescription_mapping = {'Myope': 1, 'Hypermetrope': 2}
    astigmatism_mapping = {'Yes': 1, 'No': 2}
    tear_production_mapping = {'Reduced': 1, 'Normal': 2}
    # Mapping for class transformation
    lenses_mapping = {'Yes': 1, 'No': 2}
    
    for item in dbTraining:
        features = [age_mapping[item[0]], prescription_mapping[item[1]], astigmatism_mapping[item[2]], tear_production_mapping[item[3]]]
        X.append(features)
        Y.append(lenses_mapping[item[4]])
    


    #transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
    # Y =

    #loop your training and test tasks 10 times here
    total_accuracy = 0
    for i in range (10):

       #fitting the decision tree to the data setting max_depth=3
       clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
       clf = clf.fit(X, Y)

       #read the test data and add this data to dbTest
       #--> add your Python code here
       # dbTest =
       dbTest = []
       with open('contact_lens_test.csv', 'r') as csvfile:
           reader = csv.reader(csvfile)
           for j, row in enumerate(reader):
               if j > 0:  # skipping the header
                   dbTest.append(row)
       counter = 0
       X1 = []
       Y1 = []
       for item in dbTest:
            features = [age_mapping[item[0]], prescription_mapping[item[1]], astigmatism_mapping[item[2]], tear_production_mapping[item[3]]]
            X1.append(features)
            Y1.append(lenses_mapping[item[4]])
           #transform the features of the test instances to numbers following the same strategy done during training,
           #and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
           #where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
           #--> add your Python code here
        # Predict using the trained decision tree
       predictions = clf.predict(X1)

        # Calculate accuracy for this run
       correct_predictions = sum(predictions == Y1)
       accuracy = correct_predictions / len(Y1)

        # Accumulate accuracy for averaging later
       total_accuracy += accuracy

# Calculate average accuracy over 10 runs
    average_accuracy = total_accuracy / 10

    # Print the average accuracy
    print(f'Final accuracy when training on {ds}: {average_accuracy}')
           #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
           #--> add your Python code here

    #find the average of this model during the 10 runs (training and test set)
    #--> add your Python code here

    #print the average accuracy of this model during the 10 runs (training and test set).
    #your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    #--> add your Python code here




