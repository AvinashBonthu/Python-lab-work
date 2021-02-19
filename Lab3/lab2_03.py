print "Enter the three sides of triangle"
a=input()
b=input()
c=input()
if a+b>c:
    if a+c>b:
        if b+c>a:
            print "Entered three sides form a triangle "
        else:
            print "Entered sides do not form a triangle"
    else:
            print "Entered sides do not form a triangle"
else:
            print "Entered sides do not form a triangle"
