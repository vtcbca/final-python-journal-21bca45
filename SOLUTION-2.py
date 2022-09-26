import csv
with open('salary.csv','r',newline='') as sal:
 r=csv.reader(sal)
 for i in sal:
print(i)