l=input("Enter the number of legs ")
h=input("Enter the number of heads ")
c=0
if l%2!=0:
    print "No solution"
    exit(-1)
else:
    c=(l)-2*h
    c=c/2
    print "Number of rabbits=",c
    print "Number of chickens=",h-c
