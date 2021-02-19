a=[]
b=[]
c=[]
n1=int(input("Enter the first number"))
n2=int(input("Enter the second number"))
for i in range(1,n1+1):
    if n1%i==0:
        a.append(i)
print a
for i in range(1,n2+1):
    if n2%i==0:
        b.append(i)
print b
for i in range(0,min(len(a),len(b))):
    for j in range(0,max(len(a),len(b))):
        if len(a)>len(b):
            if b[i]==a[j]:
                c.append(b[i])
        else:
            if a[i]==b[j]:
                c.append(a[i])
print c
print "G.C.D=",max(c)
