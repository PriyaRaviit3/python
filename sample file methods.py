f=open("simple.txt","w")
>>> f.write("hi migen love you")
17
>>> f=open("simple.txt","r")
>>> f.readline()
'hi migen love you'
>>> f=open("simple.txt","a")
>>> f.write("do you love me")
14
>>> f=open("simple.txt","r")
>>> f.readline()
'hi migen love youdo you love me'