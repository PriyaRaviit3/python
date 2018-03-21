 import re
>>> x=re.findall(r"","hi migen.. how are you.. i will be back in afternoon")
>>> print(x)
['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
>>> x=re.findall(r"\w","hi migen.. how are you.. i will be back in afternoon")
>>> print(x)
['h', 'i', 'm', 'i', 'g', 'e', 'n', 'h', 'o', 'w', 'a', 'r', 'e', 'y', 'o', 'u', 'i', 'w', 'i', 'l', 'l', 'b', 'e', 'b', 'a', 'c', 'k', 'i', 'n', 'a', 'f', 't', 'e', 'r', 'n', 'o', 'o', 'n']
>>> x=re.findall(r"\w\b","hi migen.. how are you.. i will be back in afternoon")
>>> print(x)
['i', 'n', 'w', 'e', 'u', 'i', 'l', 'e', 'k', 'n', 'n']
>>> x=re.findall(r"\w\B","hi migen.. how are you.. i will be back in afternoon")
>>> print(x)
['h', 'm', 'i', 'g', 'e', 'h', 'o', 'a', 'r', 'y', 'o', 'w', 'i', 'l', 'b', 'b', 'a', 'c', 'i', 'a', 'f', 't', 'e', 'r', 'n', 'o', 'o']
>>> x=re.findall(r"^\w","hi migen.. how are you.. i will be back in afternoon")
>>> print(x)
['h']
>>> x=re.findall(r"\w$","hi migen.. how are you.. i will be back in afternoon")
>>> print(x)
['n']
>>> x=re.findall(r"\w+","hi migen.. how are you.. i will be back in afternoon")
>>> print(x)
['hi', 'migen', 'how', 'are', 'you', 'i', 'will', 'be', 'back', 'in', 'afternoon']
>>> x=re.findall(r"\w*","hi migen.. how are you.. i will be back in afternoon")
>>> print(x)
['hi', '', 'migen', '', '', '', 'how', '', 'are', '', 'you', '', '', '', 'i', '', 'will', '', 'be', '', 'back', '', 'in', '', 'afternoon', '']
>>> x=re.findall(r"\w{1}","hi migen.. how are you.. i will be back in afternoon")
>>> print(x)
['h', 'i', 'm', 'i', 'g', 'e', 'n', 'h', 'o', 'w', 'a', 'r', 'e', 'y', 'o', 'u', 'i', 'w', 'i', 'l', 'l', 'b', 'e', 'b', 'a', 'c', 'k', 'i', 'n', 'a', 'f', 't', 'e', 'r', 'n', 'o', 'o', 'n']
>>> x=re.findall(r"\w{2}","hi migen.. how are you.. i will be back in afternoon")
>>> print(x)
['hi', 'mi', 'ge', 'ho', 'ar', 'yo', 'wi', 'll', 'be', 'ba', 'ck', 'in', 'af', 'te', 'rn', 'oo']
>>> x=re.findall(r"\w{3}","hi migen.. how are you.. i will be back in afternoon")
>>> print(x)
['mig', 'how', 'are', 'you', 'wil', 'bac', 'aft', 'ern', 'oon']
>>> x=re.findall(r"\w+$","hi migen.. how are you.. i will be back in afternoon")
>>> 
>>> print(x)
['afternoon']
>>> x=re.findall(r"^\w+","hi migen.. how are you.. i will be back in afternoon")
>>> print(x)
['hi']
>>> x=re.findall(r"\w\s","The regular expression language is relatively small and restricted")
>>> print(x)
['e ', 'r ', 'n ', 'e ', 's ', 'y ', 'l ', 'd ']
>>> x=re.findall(r"\w\S","The regular expression language is relatively small and restricted")
>>> print(x)
['Th', 're', 'gu', 'la', 'ex', 'pr', 'es', 'si', 'on', 'la', 'ng', 'ua', 'ge', 'is', 're', 'la', 'ti', 've', 'ly', 'sm', 'al', 'an', 're', 'st', 'ri', 'ct', 'ed']
