class file1:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return("%s i love %s" % (self.x,self.y))






# import files
#from(floder name.file name)import (class name)




from file.f import file1
r=[file1("priya","migen")]
for i in r:
    print(i)
