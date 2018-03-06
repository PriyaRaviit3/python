from .student1 import *

class staff(student):
    def __init__(self,name,age,salary):
        student. __init__(self,name,age)
        self.salary=salary
    def displaystaff(self):
        print("salary= %s" % self.salary)
