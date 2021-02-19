sroot={}
for i in range(10):
    x=input("Enter the number ")
    if x>20 and x<30:
        sroot.update({x:float(pow(x,(1/2.0)))})
print "The dictionary sroot=",sroot
