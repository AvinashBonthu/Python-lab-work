def count (i,a,c):
    if i<len(a):
        if a[i]=='a':
            c=c+1
        i=i+1
        count(i,a,c)
    else:
        print 'count of a is',c
a=raw_input('enter the string')
i=0
c=0
count(i,a,c)
