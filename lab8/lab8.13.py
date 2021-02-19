a=raw_input('Enter the string')
b=a.split()
li=[]
c=0
d=0
for i in range(int(b[0])):
    c=0
    li2=[]
    for j in range(int(b[1])):
        li2.append(c)
        c=c+d
    d+=1
    li.append(li2)
for i in range(len(li)):
    print li[i]
 
