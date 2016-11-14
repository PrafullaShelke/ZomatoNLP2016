# -*- coding: utf-8 -*-
"""
Created on Sat Nov 05 18:53:29 2016

@author: hp-pc
"""

text_file = open("C:/Users/Mr/Downloads/items.txt", "r")
items = []
itemsep = []
while True:
    tempS = text_file.readline().rstrip('\n').rstrip(' ').lstrip(' ')
    if tempS == '':
        break
    if tempS == '\n' :
        break
    temp = tempS.split(" ")
    for i in temp:
        itemsep.append(i)
    items.append(tempS)
text_file.close()
#print itemsep
#print items

import pandas as pd
#from collections import OrderedDict
import csv
from textblob import TextBlob

def csv_dict_writer(path, fieldnames, data):
    with open(path, "wb") as out_file:
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)
    
mydata = pd.read_csv("C:/Users/Mr/Downloads/after_flooding.csv")
#print mydata
x=mydata["Reviews"]
y=mydata["Rating"]
z=mydata["label"]
a=mydata["hotel"]
newreviews = [["","Rating","Reviews","hotel","label","fooditemsbylist","fooditemsfromreviews"]]
for i in range(0,len(x)-1):
    item = ""
    rev = x[i]
    itemfromreview = []
    if pd.isnull(rev):
        continue
    else:
        for itemtemp in items:
            if rev.find(itemtemp) > -1:
                item = item +","+itemtemp
#                item.append(itemtemp)
        nrev= strip_non_ascii(rev)
        blob = TextBlob(nrev)
        sentence = blob.sentences[0]
        for word, pos in sentence.tags:
            if pos == 'NN':
                itemfromreview.append(word)
    #print i
    newreviews.append([str(i), str(y[i]),nrev,a[i],z[i],item,itemfromreview])

mylist = []
fieldnames = newreviews[0]
for values in newreviews[1:]:
    inner_dict = dict(zip(fieldnames, values))
    mylist.append(inner_dict)
print "writing into file"
csv_dict_writer("C:/Users/Mr/Downloads/after_capturing_items_latest.csv",fieldnames, mylist)

