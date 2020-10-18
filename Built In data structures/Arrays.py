from array import *
#alias name

a=array('i',[1,2,3,4,5,6])

a.append(9) #can add only 1 element
a.extend([2,3,4]) # can add many elements at a time
a.insert(0,0)   #adding elements at particular position, it move other elements to rightt
a.pop() #pop can take 1 or 0 parameter
a.pop(3) #removes the element at index 3 which is element
a.remove(2) #element 2 will be remove
#print(a)
#print(len(a))


#array concatenation
#can't concatenate array which hold different data types
b=array('i',[1,2,3,4,5,6])
c=array('i',[0,5,6,7])      #here i means integer and if we use 'd' in place of i then it means floating values

d=array('i')
d=b+c
print(d[0:5])# it doesn't include 5the index
print(d[::-1]) #this method reverse array but proble is it is not preferrable as it consumes huge memory


#looping through array

for x in d:
    print(x)

temp=0
while temp<d[2]:
    print(d[temp])
    temp+=1

temp=0
while temp <len(a):
    print(a[temp])
    temp+=1


