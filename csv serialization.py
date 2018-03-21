from csv import DictReader
import pickle

data=list(DictReader(open("diabetes.csv","rt")))


data1=open("diabetes.pkl","wb")
pickle.dump(data,data1)

data1.close()

data1=open("diabetes.pkl","rb")
pickle.load(data1)


for i in data:
    print(i)