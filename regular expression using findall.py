import re
allhappy=re.findall("happy","be happy.... it gives more happy")
for i in allhappy:
    print(i)


output:
    
happy
happy






import re
month="jm,fm,mm,am,mm,jm,am,sm,am,nm,dm"
months=re.findall("[a-z]m",month)
for i in months:
    print(i)
    
    
    
    
    output:
        
        jm
        fm
        mm
        am
        mm
        jm
        am
        sm
        am
        nm
        dm

        
        
