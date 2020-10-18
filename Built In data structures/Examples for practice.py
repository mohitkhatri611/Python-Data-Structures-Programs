def primenumber():
    a=int(input("enter the number"))
    if a >1:
        for x in range(2,a):
            if (a%x)==0:
                print("not prime")
                break
            else:
                print("Prime")
                break
    else:
        prime("not prime")

def pallindrome():
    a=input('enter the string')
    b=a[::-1]
    if a==b:
        print('pallendrome')
    else:
        print('not pallendomre')


def pyramid(r):     #best metod for all 3 pymid
    for x in range(r):
        print(' '*(r-x-1)+ '*'*(2*x+1))

def fibonacciSeries():
    a=int(input("Enter the terms"))
    f=0
    s=1
    print(f,s,end=",")
    for x in range(2,a):

        next=f+s
        print(next, end=",")
        f=s
        s=next

def bubbleSort(a):
    b=len(a)-1
    for x in range(b):
        for y in range(b-x):
            if a[y]>a[y+1]:
                a[y],a[y+1]=a[y+1],a[y]
        return a
a=[3,6,1,8]
bubbleSort(a)



