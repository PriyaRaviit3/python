class student:
	def display(self,x="migen"):
		self.x=x
		print(self.x)

		
>>> s=student()
>>> s.display()
migen
>>> s.display(1)
1
