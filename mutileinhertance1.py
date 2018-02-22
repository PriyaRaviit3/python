class student:
	def __init__(self,name,age,rollno):
		self.name=name
		self.age=age
		self.rollno=rollno
	def displaystu(self):
		print("{} {} {}".format(self.name,self.age,self.rollno))

		
>>> class employee:
	def __init__(self,name,age,rollno,salary,designation):
		student.__init__(self,name,age,rollno)
		self.salary=salary
		self.designation=designation
	def displayemp(self):
		print("employee details=%s %s %s" % (self.name,self.age,self.rollno))
		print("{} {}".format(self.salary,self.designation))

		
>>> class manager(student,employee):
	def __init__(self,name,age,rollno,salary,designation,admin):
		employee.__init__(self,name,age,rollno,salary,designation)
		self.admin=admin
	def displaymanage(self):
		print("manager details= %s %s %s %s %s" % (self.name,self.age,self.rollno,self.salary,self.designation))
		print("{}".format(self.admin))

		
>>> obj=manager("migen",2,6,60000,"engineer","yes")
>>> obj.displaystu()
migen 2 6
>>> obj.displayemp()
employee details=migen 2 6
60000 engineer
>>> obj.displaymanage()
manager details= migen 2 6 60000 engineer
yes
>>> print(student.__doc__)
None
>>> print(employee.__module__)
__main__
>>> print(manager.__name__)
manager
>>> print(manager.__bases__)
(<class '__main__.student'>, <class '__main__.employee'>)
>>> 
