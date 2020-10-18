a={1,2,4,'aaa','abc',8,9}

b=set([1,4,3,'abc',87])

a.update([2,'abc',7])   #pass list of elements
a.add('dfdf')   #add only one element
a.remove('aaa')  #throw error if element not presetn
a.discard('ab')
a.pop() #pop random element

print(a)
#union methods two ways using pipline or function

print(a|b)      #first method using pipeline
print(a.union(b))   #second method using function union



#.....intersection of set
#common element in all the set
#two ways

print(a&b)
print(a.intersection(b))

#differece of set.....
print(a-b) #way 1
print(a.difference(b))  #way 2

#frozen set -> it will make set immtable  means can't modify the value
d=frozenset(a)
d.add(90)   #error because of this........
