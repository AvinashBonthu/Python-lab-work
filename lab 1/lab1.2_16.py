a=[]
b=[]
c=0
print 'Enter The numbers'
for i in range(0,10):
    p=int(input())
    a.append(p)
t=0
while(t<10):
    if a[t]%2!=0:
        b.append(a[t])
        c+=1
    t+=1
if c!=0:
    print "The maximum number is=",max(b)
else:
    print 'There are no odd numbers in the entered numbers'
            
    
