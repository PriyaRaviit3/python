 class student:

	def __init__(self,name,age,rollno):
		self.name=name
		self.age=age
		self.rollno=rollno
	def display(self):
		print("my name is {}" .format(self.name))
		print("my age is {}" .format(self.age))
		print("my rollno is {}" .format(self.rollno))

		      
>>> s=student("migen",2,6)
		      
>>> s.display()
		      
my name is migen
my age is 2
my rollno is 6
>>> student.school="sankar"
		      
>>> s.school
		      
'sankar'
>>> s.__dict__
		      
{'name': 'migen', 'age': 2, 'rollno': 6}
>>> getattr(s,"school")
		      
'sankar'
>>> if(getattr(s,"school")):
	print("my school name is {}".format(s.school))

		      
my school name is sankar
>>> s.display()
		      
my name is migen
my age is 2
my rollno is 6
>>> 
