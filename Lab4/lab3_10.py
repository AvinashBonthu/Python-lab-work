n=input("Enter number of elements in list")
a=[]
for i in range(n):
    r=input("Enter the element ")
    a.append(r)
for i in a:
    if type(i)==list:
        for j in i:
            print j,
    else:
        print i,
