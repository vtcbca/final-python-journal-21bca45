import csv
with open('salary.csv','r',newline='') as sal:
 data=csv.DictReader(sal)
 l=[]
 s=0
 for i in data:
    d=i['Department']
 if d=='BCA':
    s+=int(i['Salary'])
 print('The total Salary of BCA Department is : {}'.format(s))