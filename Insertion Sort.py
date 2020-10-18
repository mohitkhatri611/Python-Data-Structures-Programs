def isort(a):
    for x in range(1, len(a)):
        k = a[x] # element present at index number 1
        j=x-1
        while j >= 0 and k < a[j]: #comparing element with the next until the last item
                a[j+1] = a[j]
                j -= 1
        a[j+1] = k

a=[23,56,1,50,17]
isort(a)
print(a)
