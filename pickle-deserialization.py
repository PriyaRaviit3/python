import pickle

list={1:["migen",2,2],2:["priya",3,3]}


with open("e:\green java\data1.pkl","wb") as files:
    pickle.dump(list,files)
    del(list)


filesin=open("e:\green java\data1.pkl","rb")
print(pickle.load(filesin))



output:
{1: ['migen', 2, 2], 2: ['priya', 3, 3]}
