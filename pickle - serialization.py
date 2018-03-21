class student:
    def __init__(self, name, age, rollno):
        self.name = name
        self.age = age
        self.rollno = rollno

    def display(self):
        print("my name is %s = " % self.name)
        print(" my age is %s= " % self.age)
        print(" my rollno is %s= " % self.rollno)

s = student("migen", 3, 6)


with open("e:\green java\data2.pkl","wb") as data:
        pickle.dump(s, data)


with open("e:\green java\data2.pkl","rb") as data:
        print(pickle.load(data))




output:
<__main__.student object at 0x052BB4F0>
