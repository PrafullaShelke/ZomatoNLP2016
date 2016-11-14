import pandas as pd
#from collections import OrderedDict
import csv
def csv_dict_writer(path, fieldnames, data):
    with open(path, "wb") as out_file:
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
def check(word, l) :
    temp = word[l]
    a = l+1
    while a < len(word):
        if temp  == word[a]:
            a = a+1
        else:
            break
    return a-l
    
mydata = pd.read_csv("C:/Users/Mr/Downloads/after_flooding.csv")
#print mydata
x = mydata["Reviews"]
y=mydata["Rating"]
z=mydata["label"]
a=mydata["hotel"]
newreviews = [["","Rating","Reviews","hotel","label"]]
for i in range(0,len(x)-1):
    newreview = ""
    words = x[i].split(" ")
#    print words
    for k in range(0,len(words)-1):
        #flooding removal
        word = words[k]
        nword = []
        l=0
        value =1
        while l <len(word)-1 :
            value = check(word, l)
            if value == 1:
                nword.append(word[l])
                l =l+1
            else:
                nword.append(word[l])
                nword.append(word[l])
                l = l+value
        if value <= 2 and len(word) > 0:
            nword.append(word[len(word)-1])
            
        newword = ''.join(map(str, nword))        
        newreview = newreview + " " + newword
        #        if words[k] != "good" and words[k] != "non": 
#            newreview = newreview + " " + ("".join(OrderedDict.fromkeys(words[k])))
#        else:
#            newreview = newreview + " " + words[k]
    newreviews.append([str(i), str(y[i]),newreview,a[i],z[i]])

mylist = []
fieldnames = newreviews[0]
for values in newreviews[1:]:
    inner_dict = dict(zip(fieldnames, values))
    mylist.append(inner_dict)
print("writing into file")
csv_dict_writer("D:/KGP/SNLP/project/after_flooding.csv",fieldnames, mylist)
