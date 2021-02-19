n=input("Enter the number of elements ")
a=[]
c=0
for i in range(n):
    r=input("Enter the element ")
    a.append(r)
for i in range(n-1):
    if a[i]==a[i+1]:
        c+=1
print c
