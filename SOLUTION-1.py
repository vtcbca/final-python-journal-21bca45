import csv
with open('salary.csv','w',newline='') as sal:
 data=[['Empid','Empname','Department','Experience','Salary'],
 [1,'ABC','BCA','4 Years',40000],
 [2,'DEF','BBA','3 Years',30000],
 [3,'GHI','MCA','2 Years',20000],
 [4,'JKL','MBA','3 Years',30000],
 [5,'MNO','MCA','5 Years',50000]]
 w=csv.writer(sal)
 w.writerows(data)
 print('Data are Successfully Written.')