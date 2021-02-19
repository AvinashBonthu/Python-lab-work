def palindrome(a):
    b=a[::-1]
    if a==b:
        print 1
    else:
        print 0
a=raw_input('enter the string ')
palindrome(a)
