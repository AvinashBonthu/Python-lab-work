a=raw_input("Enter the string ")
vo=['a','e','i','o','u'," "]
b=[]
for i in a:
    if(i not in vo):
        i=i+"o"+i
    b.append(i)
c=""
c=c.join(b)
print c
    

        
