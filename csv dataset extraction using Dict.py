import csv
f=open("e:\green java\Answers.csv","r")
c_name=[]
csv_data=csv.DictReader(f)
for row in f:
    print(row[0])
    
