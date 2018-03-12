dict={"name":"priya","age":27,"place":"sankari"}
>>> dict
{'name': 'priya', 'age': 27, 'place': 'sankari'}
>>> dict{"name"}
SyntaxError: invalid syntax
>>> dict["name"]
'priya'
>>> dict["age"]
27
>>> dict["place"]
'sankari'
>>> dict1=dict.copy()
>>> dict1
{'name': 'priya', 'age': 27, 'place': 'sankari'}
>>> dict.keys()
dict_keys(['name', 'age', 'place'])
>>> dict.values()
dict_values(['priya', 27, 'sankari'])
dict={"name":"priya","age":27,"place":"sankari"}
>>> dict
{'name': 'priya', 'age': 27, 'place': 'sankari'}
>>> dict{"name"}
SyntaxError: invalid syntax
>>> dict["name"]
'priya'
>>> dict["age"]
27
>>> dict["place"]
'sankari'
>>> dict1=dict.copy()
>>> dict1
{'name': 'priya', 'age': 27, 'place': 'sankari'}
>>> dict.keys()
dict_keys(['name', 'age', 'place'])
>>> dict.values()
dict_values(['priya', 27, 'sankari'])
 dict["state"]="tamilnadu"
>>> dict
{'name': 'priya', 'age': 27, 'place': 'sankari', 'state': 'tamilnadu'}
>>> dict={"name":"priya","age":27,"place":"sankari"}
>>> dict
{'name': 'priya', 'age': 27, 'place': 'sankari'}
>>> dict.update({"son":"migen"})
>>> dict
{'name': 'priya', 'age': 27, 'place': 'sankari', 'son': 'migen'}
>>> dict.values()
dict_values(['priya', 27, 'sankari', 'migen'])
>>> dict.keys()
dict_keys(['name', 'age', 'place', 'son'])
>>> dict={1:{"name":"priya","age":27,"place":"sankari"},2:{"name":"migen","age":3,"place":"sankari"},3:{"name":"santhosh","age":32,"place":"sankari"}}
>>> dict
{1: {'name': 'priya', 'age': 27, 'place': 'sankari'}, 2: {'name': 'migen', 'age': 3, 'place': 'sankari'}, 3: {'name': 'santhosh', 'age': 32, 'place': 'sankari'}}
>>> dict[1]
{'name': 'priya', 'age': 27, 'place': 'sankari'}
>>> dict[2]
{'name': 'migen', 'age': 3, 'place': 'sankari'}
>>> dict[3]
{'name': 'santhosh', 'age': 32, 'place': 'sankari'}
 dict[4]={"name":"bavyaa","age":23,"place":"sankari"}
>>> dict
{1: {'name': 'priya', 'age': 27, 'place': 'sankari'}, 2: {'name': 'migen', 'age': 3, 'place': 'sankari'}, 3: {'name': 'santhosh', 'age': 32, 'place': 'sankari'}, 4: {'name': 'bavyaa', 'age': 23, 'place': 'sankari'}}
 import sys
>>> sys.path
['', 'C:\\Users\\STUDENT\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\idlelib', 'C:\\Users\\STUDENT\\AppData\\Local\\Programs\\Python\\Python36-32\\python36.zip', 'C:\\Users\\STUDENT\\AppData\\Local\\Programs\\Python\\Python36-32\\DLLs', 'C:\\Users\\STUDENT\\AppData\\Local\\Programs\\Python\\Python36-32\\lib', 'C:\\Users\\STUDENT\\AppData\\Local\\Programs\\Python\\Python36-32', 'C:\\Users\\STUDENT\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages']
for i in sys.path:
	print(i)

	

C:\Users\STUDENT\AppData\Local\Programs\Python\Python36-32\Lib\idlelib
C:\Users\STUDENT\AppData\Local\Programs\Python\Python36-32\python36.zip
C:\Users\STUDENT\AppData\Local\Programs\Python\Python36-32\DLLs
C:\Users\STUDENT\AppData\Local\Programs\Python\Python36-32\lib
C:\Users\STUDENT\AppData\Local\Programs\Python\Python36-32
C:\Users\STUDENT\AppData\Local\Programs\Python\Python36-32\lib\site-packages