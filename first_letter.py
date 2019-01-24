#!/usr/bin/python
#prints first letter of list of strings

import csv

with open("input.txt") as file: 
    reader = csv.reader(file, delimiter=' ')
    for row in reader:
        name = row[0]
        print (name[0])
