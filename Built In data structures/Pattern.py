#pyramid
#The above end= argument causes a space to be printed after each number, rather than the default newline character.
#The print() function also has a sep= keyword argument which controls what gets printed between items:
# print('foo', 'bar', 'baz', sep='+++')
#foo+++bar+++baz
"""
for x in range(5):
    i=5
    print(' '*(i-x)+ ' *' * (x+1))


#other way

def pattern(n):
    k=2*n-2 #specifying the space
    for i in range(0,n):
        for j in range(0,k):
            print(end= " ")
        k=k-1
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
pattern(5)

#inverse pattern pyramid
def pattern(n):
    k = n
    for i in range(n,-1,-1): #using this we can specify the backward direction
        for j in range(k,0,-1): #-1 for backward direction
            print(end=" ")
        k=k+1
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
pattern(5)
#right start pattern
def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
    for i in range(n,-1,-1):
        for j in range(0,i+1):
            print("* ", end="")
        print("\r")
#way 2

def pattern(n):
    k=n
    for i in range(n):
        print('* ' * i )

    for i in range(n-1,0,-1):
        print('* '* i)

#left start pattern
def pattern(n):
    k= 2*n - 2
    for i in range(0,n-1):
        for j in range(0,k):
             print(end=" ")
        k=k-2
        for j in range(0,i+1):
            print('* ',end="")
        print('\r')
    k=k-1

    for i in range(n-1,-1,-1):
        for j in range(k,-1,-1):
            print(end=" ")
        k=k+2
        for j in range(0,i+1):
            print("* ",end="")
        print('\r')
pattern(10)


#hourglass
def pattern(n):
    k=n-2
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end=" ")
        k+=1
        for j in range(0,i+1):
            print("* ",end="")
        print('\r')
    k= 2* n - 2
    for i in range(0,n+1):
        for j in range(k):
            print(end=" ")
        k=k-1
        for j in range(i+1):
            print('* ',end="")
        print('\r')


pattern(5)
"""




