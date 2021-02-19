import math
odd={}
for i in range(51):
    if i%2!=0:
        odd.update({i:math.log(i,2)})
print "The dictionary odd=",odd
