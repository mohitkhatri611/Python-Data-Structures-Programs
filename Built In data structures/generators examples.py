#use to produce iterators
#Better memory and utilization
#produce infinite items
#can also be used to pipeline a number of operations
#it produce one item at single time

def new(dict):
    for x,y in dict.items():
        yield x,y
a={1:'hi',2:'welcome'}
b=new(a)    #creating b as generator obect
#print(b)
#print(next(b))
#print(next(b))

#using the function
def myfunction(i):
    while i<=3:
        yield i
        i+=1

j=myfunction(2)
#next(j)
#print(next(j))
#print(next(j))

#example of two parts in function
"""
def ex():
    n=3
    yield n
    n=n*n
    yield n

v=ex()
for x in v:     #after all execute iteration it stopped the iteration
    print(x)

#how to use generator expressions

f=range(6)
print("list comp",end=":")
q=[x+2 for x in f]
print(q)
print("list comp",end=":")
r=[x+2 for x in f]
print(r)

for x in r:
    print(x)

#find int the min value
f=range(6)
print('gen exp',end=":")
r=(x+2 for x in f)
print(r)
print(min(r))


"""
#..........use cases
#example using fibonacci series
"""
def fib():
    f,s=0,1
    while True:
        yield f
        f,s=s,f+s
for x in fib():
    if x> 50:
        break
    print(x,end=" ")
   """

#number stream

a=range(2,100,2) # for even number for odd -> (1,100,2)
b=(x for x in a)
print(b)
for y in b:
    print(y)








