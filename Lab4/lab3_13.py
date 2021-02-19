e=["181B001","181B002","181B003","181B004","181B005","181B006","181B007","181B008","181B009","181B010"]
n=["Ram","Shyam","Riya","Atul","Bittu","Munna","Raju","Sarath","Sneha","Rama"]
u=input("Enter the enrollment number you want to search ")
if u in e:
    p=e.index(u)
    print "Enrollment number= ",u,"Name= ",n[p]
else:
    print "-1"
