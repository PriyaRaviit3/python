with open("simple.txt","w+") as f:
	f.write("hi migen")

	
8
>>> with open("simple.txt","r") as f:
	f.readline()

	
'hi migen'
>>> with open("simple.txt","a") as f:
	f.write(" love you")

	
9
>>> with open("simple.txt","r") as f:
	f.readline()

	
'hi migen love you'
>>> f.closed
True