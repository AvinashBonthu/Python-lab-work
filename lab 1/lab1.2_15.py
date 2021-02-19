n=int(input("Enter the no "))
s=0
while n!=0:
    k=n%10
    if k==9:
        k=0
    else:
        k+=1
    s=s*10+k
    n=n/10
p=0
while s!=0:
    r=s%10
    p=p*10+r
    s=s/10
print p
