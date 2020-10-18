#we have implemented the stack using the two methods
#Method 1 using the normal list
""""
stack=[]

def empty():
    if len(stack)==0:
        print('Stack is empty.\n')
    else:
        print(stack, '\n')


val1 = 1
val2 = 2
val3 = 3

stack.append(val1)
stack.append(val2)
stack.append(val3)

empty()
a=stack.pop()
b=stack.pop()
c=stack.pop()

print('The popped elements are: ',a,b,c, '\n')
empty()
"""
#Method 2 using the class and it is more interactive

class Stack:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return self.items ==[]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()


s=Stack()
while True:
    print('1.Push')
    print('2.Pop')
    print('3.Quit')
    do= int(input('what would you like to do?: '))
    if do==1:
        val=input('Enter the value: ')
        s.push(val)
    elif do==2:
        if s.is_empty():
            print('Stack is empty \n')
        else:
            print('Popped value: ',s.pop())

    elif do==3:
        break