import re
str="""hi migan,
        how are you,
        love you"""
y=re.compile("migan")
print(y.sub("migen",str))


output:

    hi migen,
        how are you,
        love you
