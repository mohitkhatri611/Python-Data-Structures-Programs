
#Range(start,stop, step or number of times the skip will happen)
b=range(0,11,2)

#using with loops
for i in range(0,10,2):
    print(i,end=' ')
#python 3 dones't have xrange()
#frange(start,stop,step) but it is in jupiter only
#for j in frange(0.1,1.0,0.2):
 #   print(j)

#reverse range in python
print("reverse range")
for i in range(5,0,-1):#  range(start,stop, steps can be dec(-ve) or inc(+ve value )
    print(i,end="")

#concatenation of two range functions
print("")
from itertools import chain
res=chain(range(10),range(10,21))   #res means result her we concatenate two range using chain

for i in res:
    print(i, end=", ")

print("")
#accessing the elements in range function using indexes

a=range(4,10)[3] #At index 3  the element is 7 we know
b=range(2,5)[2]
print(a, b)

print("")
#converting a range to list
"""very very important----------"""
a=range(0,10,2)
b=list(a)
c=list(range(0,10))
print(b)
print(c)

#use range for +ve and -ve step value

for i in range (10,-8,-2):
    print(i, end=" ")