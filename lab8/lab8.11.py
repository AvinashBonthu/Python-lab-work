def is_member(x,a):
    c=0
    for i in range(len(a)):
        if x==a[i]:
            print 1
            c=c+1
            break
    if c==0:
        print 0
            
x=raw_input('enter any value')
a=raw_input('enter the list of values')
is_member(x,a)
