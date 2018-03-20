import re
str="hi migen love you... i know you too love me "
for i in re.finditer("migen",str):
    x=i.span()
    print(x)



output:

(3,8)   #it mention a name of migen starting and ending point