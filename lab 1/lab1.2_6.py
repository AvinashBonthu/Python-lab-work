t=float(input("Enter the total number of marks"))
s=[]
a=0
for i in range (0,6):
    print "Enter the subject {} marks".format(i)
    m=int(input())
    s.append(m)
    a=a+s[i]
print 'Percentage of student='
print (a/t)*100

