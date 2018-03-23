import re
def display(string):
    x=re.compile(r"[^a-zA-Z0-9]")
    string=x.search(string)
    return not bool(string)
print(display("ABCDEFabcdef123450"))
print(display("!@#$%^&*)(}{"))




#output:

True
False
