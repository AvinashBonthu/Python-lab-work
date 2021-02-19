l=[]
x=input("Enter the year ")
x=x+1
c=0
while(1):
    if x%4==0:
        if x%100==0:
            if x%400==0:
                l.append(x)
                c+=1
        else:
            l.append(x)
            c+=1
    x+=1
    if(c==15):
        break
print "List of leap years =",l
                
