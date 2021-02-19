def prime (a,b):
    a=a+1
    flag=0
    if a!=b:
        
        
        for i in range(a):
            i=i+2
            
            if a%i==0:
                flag=1
                
    if flag ==0:
        print a
        prime(a,b)
    if a!=b:
        prime(a,b)
a=input('enter starting position')
b=input('enter ending position')
prime(a,b)
