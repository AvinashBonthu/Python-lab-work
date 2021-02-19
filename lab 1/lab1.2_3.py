p=float(input("Enter the principle amount="))
R=float(input('Enter the rate of interest in percentage='))
t=float(input('Enter the time period in months='))
r=R/100
T=t/12
print 'simple interest is='
print p*(1+r*T)
n=int(input("Enter number of times interest should be compounded="))
print 'compund interest ='
print p*((1+(r/T))**(n*T))
