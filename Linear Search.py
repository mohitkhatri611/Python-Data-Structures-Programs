def lin_search(myarray, n, key):
    for x in range(0,n):
        if(myarray[x]==key):
            return x
    return -1


myarray=[12,1,34,17,23,6,5]
key=6
n=len(myarray)
matched=lin_search(myarray,n,key)
if(matched==-1):
    print("key is not present")
else:
    print("key is present in the given list at index",matched)
