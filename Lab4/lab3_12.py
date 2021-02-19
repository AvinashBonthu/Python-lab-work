n=input("Enter the number of elements ")
a=[]
for i in range(n):
    r=input("Enter the elements ")
    a.append(r)
print "List entered=",a
print "Least value=",min(a)
print "Highest value=",max(a)
for i in a:
    if max(a)==i:
        p=a.index(i)
    if min(a)==i:
        q=a.index(i)
a[p],a[q]=a[q],a[p]
print "List after swapping=",a
