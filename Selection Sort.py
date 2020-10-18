def selsort(myarray, r):
    for x in range(r):
        min=x # first element is assumed to be the minimum
        for y in range( x+1, r):
            if myarray[y] < myarray[min]: # compaing min with the next element
                min = y
            (myarray[x],myarray[min])= (myarray[min],myarray[x]) #swap element if required

mylist=[34,23,1,67,4]

r=len(mylist)
selsort(mylist,r)
print(mylist)