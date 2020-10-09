import numpy as np
import math
import re

def calc_angle(x, y):
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    cos_theta = np.dot(x, y) / (norm_x * norm_y)
    theta = math.degrees(math.acos(cos_theta))
    return theta


def angle (document, query):
    splitted_document = document.split(" ")
    splitted_query = query.split(" ")
    dictionary = {}
    for word in splitted_document:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word]+=1
    array = []
    array2 = []
    for word in dictionary:
        array.append(dictionary[word])
    for i in range(0,len(array)):
        array2.append(0)
    for q in splitted_query:
        for i in range(0,len(array)):
            if q == list(dictionary)[i]:
                array2[i]=1
    a = np.array(array)
    b = np.array(array2)
    """print(array)
    print(array2)"""
    return (calc_angle(a,b))

docfile = open("docs.txt", "r") 
queryfile = open("queries.txt","r")
documents = []
merge = ""
dictionary = {}
list_of_document_IDs = {}
queries = []

inverted = {}

text=[]
regex = re.compile(r'[\n\t\r]')
for line in docfile:
    documents.append(regex.sub(" ",line).strip())

for x in enumerate(documents,1):
    list_of_document_IDs[x[0]]=x[1]

for line in queryfile:
    queries.append(line.rstrip())

for x in documents:
    merge = merge + x + " "

docfile.close()
queryfile.close()

words = merge.split(" ")
words.remove("")
for word in words:
    if word not in dictionary:
        dictionary[word] = 1
    else:
        dictionary[word]+=1

for x in dictionary:
    inverted[x] = []
    for i in range(1,len(list_of_document_IDs)+1):
        if x in list_of_document_IDs[i]:
            inverted[x].append(i)

print("Words in dictionarytionary:",len(dictionary))

relevant = []
temporary = []
for q in queries:
    relevant.clear()
    temporary.clear()
    
    print(f"Query: {q}")
    print("Relevant documets: ", end= "")
    sep = q.split(" ")
    for b in sep:
        if b not in dictionary:
            sep.remove(b)
    for x in list_of_document_IDs:
        if set(sep).issubset(list_of_document_IDs[x].split()):
            relevant.append(x)

    for i in relevant:
        print(i,end=" ")
    #print(relevant)
    print()
    for i in relevant:
        print(i,round(angle(documents[i-1],q),2))
    print("")
