#-------------------------------------------------------------------------
# AUTHOR: David Bohon
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4250- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

#importing some Python libraries
import csv

documents = []
labels = []

#reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append (row[0])
            labels.append(row[1])

#Conduct stopword removal.
#--> add your Python code here
stopWords = {'I', 'and', 'She', 'They', 'her', 'their'}
for i in documents:
  for a in stopWords:
    documents[i].replace(a, "")
    
    

#Conduct stemming.
#--> add your Python code here
stemming = {
  "cats": "cat",
  "dogs": "dog",
  "loves": "love",
}
for i in documents:
  for a in stemming.keys():
    documents[i].replace(a, stemming[a])
    
#Identify the index terms.
#--> add your Python code here
terms = []
for i in documents:
  line = i.split()
  for x in line:
    terms.append(x)
termSet = set(terms)
terms = list(termSet)

#Build the tf-idf term weights matrix.
#--> add your Python code here
# Builds a dictionary that lists the total occurence of each term
# This will be used for df calculation
termCount = {}
####Dictionary initialized with all values as zero
for x in terms:
  termCount = {x:0}
############################
####Every line of every document is cycled through and the terms are counted
for i in documents:
  line = i.split()
  for a in terms.keys():
    for x in line:
      if a in x:
        termCount[a] += 1
############################
# Builds dictionary that lists the number of documents each term occurs in
docCount = {}
for x in terms:
  docCount = {x:0}
for i in documents:
  for j in docCount.keys():
    if j in  i:
      docCount[j] += 1
###########################

docMatrix = []
index = []
count = 0
for i in documents:
  for j in terms:
    index[count].append(0)
  count += 1


docMatrix = []

#Calculate the document scores (ranking) using document weigths (tf-idf) calculated before and query weights (binary - have or not the term).
#--> add your Python code here
docScores = []

#Calculate and print the precision and recall of the model by considering that the search engine will return all documents with scores >= 0.1.
#--> add your Python code here