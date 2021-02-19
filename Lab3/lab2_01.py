Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:22:17) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> tup1=(5,10,15,20,25)
>>> print(len(tup1))
5
>>> print(tup1[4])
25
>>> print(tup1[5])

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(tup1[5])
IndexError: tuple index out of range
>>> print(tup1[4:5])
(25,)
>>> tup1[2]
15
>>> print(tup1)
(5, 10, 15, 20, 25)
>>> tup1=tup1+(8,9)
>>> tup1
(5, 10, 15, 20, 25, 8, 9)
>>> a=[1,2,3,4]
>>> b=[5,6,7,8]
>>> a+b
[1, 2, 3, 4, 5, 6, 7, 8]
>>> a="AVI"
>>> b="NASH"
>>> a+b
'AVINASH'
>>> 
============ RESTART: N:/Advanced programming lab/Lab2/lab2_02.py ============
Enter the gems requiredRuby

Traceback (most recent call last):
  File "N:/Advanced programming lab/Lab2/lab2_02.py", line 3, in <module>
    g=input("Enter the gems required")
  File "<string>", line 1, in <module>
NameError: name 'Ruby' is not defined
>>> 
