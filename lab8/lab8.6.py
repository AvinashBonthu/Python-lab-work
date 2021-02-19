a=raw_input()
x=1
for i in a:
    c=0
    for j in a[x::]:
        if i==j:
            
            c=c+1
    if c==0:
        print "the 1st non repeating character is ",i
        break
    x=x+1
