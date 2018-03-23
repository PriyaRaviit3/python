#http://regexlib.com/CheatSheet.aspx
#text match



import re
def text_match(text):
    pattern="ab*?"

    if re.search(pattern,text):
        return"found a match"
    else:
        return"not match"
print(text_match("ca"))
print(text_match("abc"))
print(text_match("abbc"))



#output:


found a match
found a match
found a match
