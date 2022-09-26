import csv
with open('salary.csv','a',newline='') as sal:
 data=[[6,'PQR','BCA','6 Years',60000],
 [7,'XYZ','MBA','4 Years',40000]]
 w=csv.writer(sal)
 w.writerows(data)