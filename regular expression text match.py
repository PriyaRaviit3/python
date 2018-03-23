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





import re
def text_match(text):
    pattern="ab{7}"

    if re.search(pattern,text):
        return"found a match"
    else:
        return"not match"
print(text_match("ca"))
print(text_match("abc"))
print(text_match("abbc"))



#output:

not match
not match
not match




import re
def text_match(text):
    pattern="^[a-z]+_[a-z]+$"

    if re.search(pattern,text):
        return"found a match"
    else:
        return"not match"
print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))


#output:


found a match
not match
not match





import re
pattern = 'fox'
text = 'The quick brown fox jumps over the lazy dog.'
match = re.search(pattern, text)
s = match.start()
e = match.end()
print('Found "%s" in "%s" from %d to %d ' % \
    (match.re.pattern, match.string, s, e))




#output:



Found "fox" in "The quick brown fox jumps over the lazy dog." from 16 to 19 

