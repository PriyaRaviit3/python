import csv
data=open("e:\green java\Dataset\comptab_2018-01-29 16_00_comma_separated.csv","r")
data.read()
csv_data=csv.reader(data)
name=[]
webout=""
for line in csv_data:
    names.append(f"{line[2]}")
    webout+='<html>'
    webout+='\n<body>'
    webout+=f"\n welcome to the solution of your problem{len(names)}<\h1>"
    webout+='\n<ol>'
    for name in names:
        if(name=='UST'):
            break
        webout+=f"\n<li>{name}<\li>"
        webout+='\n<\ol>'
        webout+='\n<\body>'
        webout+='\n<\html>'
        print(webout)
