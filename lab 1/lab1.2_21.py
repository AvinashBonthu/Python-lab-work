n1=int(input("Enter the first number "))
n2=int(input("Enter the second number "))
if n1>=n2 and n1%n2==0:
    print "LCM=",n1
elif n2>=n1 and n2%n1==0:
    print "LCM=",n2
else:
    print "LCM=",n1*n2

    
