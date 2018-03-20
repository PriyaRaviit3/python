import re
if(re.search("happy","smile it gives happiness...happy")):
    print("happy found")




output:

happy found






import re
myphone="98-94-69-9690"
if re.search(r"\w{3},\w{2},\w{2},\w{4}",myphone):
    print("valid")
else:
    print("not valid")


output:

not valid
