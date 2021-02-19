a=('Emerald','Ivory','Jasper','Ruby','Garnet')
b=(1760,2119,1599,3290,3999)
i=1
cost=0
p=0
x=()
while i!=0:
    g=input("Enter the gems required ")
    if g in a: 
        n=input("Enter the number of gems required ")
        c=a.index(g)
        cost=cost+n*b[c]
        m=input("Enter 1 if you want to purchase more else 0")
        i=m
        x=x+((g,b[c]))
    else:
        print "The material is not available Total bill amount is=-1"
        p+=1
        break
if p!=1:
    if cost>=30000:
        cost=cost-(cost*5)/100.0
        print "The total bill is =",cost
    else:
        print "The total bill=",cost
print x  
