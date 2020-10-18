"""
def pattern(n):
    for i in range(0,n):
        for j in range(i+1):
            print(i+1, end=" ")
        print('\r')


#pascals traiangle
def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print(function(i,j)," ",end="")
        print()         #...............Observe

def function(n,k):
    res=1
    if (k>n -k):
        k=n-k
    for i in range(0,k):
        res=res*(n-i)
        res=res//(i+1)
    return res


def pattern(n):
    for i in range(n,0,-1):
        for j in range(1,i+1,1):
            print(j,end=" ")
        print('\r')


def pattern(n):
    k=2*n-2
    for i in range(0,n):
        for j in range(k,0,-1):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            print("10",end="")
        print("\r")



#Right alphabetical triangle
def pattern(n):
    x=65
    for i in range(0,n):
        ch=chr(x)
        x=x+1
        for j in range(0,i+1):
            print(ch,end=" ")
        print('\r')


#character pyramid
def pattern(n):
    k=2*n-2
    x=65
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            ch=chr(x)
            print(ch,end=" ")
            x=x+1
        print('\r')

# k shape pattern
for i in range(7):
    for j in range(7):
        if j ==0 or i-j==3 or i+j==3:
            print("*",end="")
        else:
            print(end=" ")
    print()

"""

def pattern(n):
    k=2*n-2
    x=65
    for i in range(0,n):
        ch=chr(x)
        x=x+1
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            print(ch,end=" ")
        print('\r')
    k=n-2
    x=65
    for i in range(n,-1,-1):
        ch=chr(x)
        x=x+1
        for j in range(k,0,-1):
            print(end=" ")
        k=k+1
        for j in range(0,i+1):
            print(ch,end=" ")
        print('\r')
pattern(15)
