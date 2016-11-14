# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 13:12:53 2016

@author: Vonteru KondalaRao and co...
"""


import pandas as pd
#from collections import OrderedDict
import csv

def csv_dict_writer(path, fieldnames, data):
    with open(path, "wb") as out_file:
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

    
mydata = pd.read_csv("C:/Users/Mr/Downloads/after_capturing_items_latest.csv")
#print mydata
reviews=mydata["Reviews"]
rating=mydata["Rating"]
z=mydata["fooditemsbylist"]
hotel=mydata["hotel"]
newreviews = [["hotel","fooditems"]]
hoteldict = {}
#for i in range(0,11):
for i in range(0,len(reviews)-1):
    items = str(z[i]).split(",")
    items = items[1:len(items)]
    if rating[i] >=4 and len(items) >0:
        hotelname  = hotel[i]
     #   print items
        try:
            aco = hoteldict[hotelname]
            for j in items:
                aco.append(j)
            hoteldict.update({hotelname: aco})
        except Exception, e:
            listitems = []
            for j in items:
                listitems.append(j)
            hoteldict.update({hotelname: listitems})

for i in hoteldict:
    listitems = list(set(hoteldict[i]))
    newreviews.append([i, listitems])
#print newreviews    
mylist = []
fieldnames = newreviews[0]
for values in newreviews[1:]:
    inner_dict = dict(zip(fieldnames, values))
    mylist.append(inner_dict)
print("writing into file")
csv_dict_writer("C:/Users/Mr/Downloads/food_items_list_for_a_hotel.csv",fieldnames, mylist)

