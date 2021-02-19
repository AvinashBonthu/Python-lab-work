prime={}
for i in range(50,101):
    p=1
    c=0
    s=0
    while(p<=i):
        if i%p==0:
            c+=1
        p+=1
    if c==2:
        n=i
        while(i):
            r=i%10
            s=s+r
            i=i/10
        prime.update({n:s})
print "The dictionary prime=",prime
