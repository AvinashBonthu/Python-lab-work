import math
n=int(input("Enter the number"))
i=1
c=0
while i>0:
    if pow(i,3)==n:
        c+=1
        break
    i+=1
if c==1:
    print "Number is a perfect cube",round(pow(n,1/3.0))
else:
    print"Number is not a perfect cube"

