class Node:
    def __init__(self,data):
        self.data= data
        self.next=None


class LinkedList:

    def __init__(self):
        self.head=None


    #function to insert new node at the beginning
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head = new_node

    def reverse(self):
        cur=self.head
        prev=None
        while cur is not None:
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next

        self.head=prev

    def reverse2(self,head):

        #if head is empyt or has reached the list end.
        if head is None or head.next is None:
            return head

        #Reverse the list
        rest = self.reverse2(head.next)
        head.next.next=head
        head.next= None
        return rest

    def printList(self):
        temp= self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next

    def reverseUtil(self,curr,prev):

        #if last node mark it head
        if curr.next is None:
            self.head=curr

            #update next to prev node
            curr.next = prev
            return

        #save curr.next node ofr rucurseve call
        next =curr.next

        #and update next
        curr.next =prev

        self.reverseutil(next,curr)

    def reverse3(self):
        #A Simpler and Tail Recursive Method
        if self.head is None:
            return
        self.reverseUtil(self.head, None)

    def reverseLLUsingStack(self):
        #this mentod will based on stack, it will store  the node in the Stack
        #unitl all values are entered. So
        """
        Once all entries are done, Update the Head pointer to the last location(i.e the last value).
        Start popping the nodes(value and address) and store them in the same order until the stack is empty.
        Update the next pointer of last Node in the stack by NULL.
        """

        #initialize the variables
        stack=[]
        temp=self.head

        while temp:
            stack.append(temp)
            temp=temp.next

        self.head=temp=stack.pop()

        while len(stack) > 0:
            ele=stack.pop()
            temp.next=ele
            temp=ele

        ele.next= None #carefull otherwise it will create infinite loop
        return



        # print("\nprinting reverse 1")
        # for i in stack:
        #     print(i.data)



if __name__=="__main__":

    llist=LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(85)

print("given Linked list")
llist.printList()
#llist.head=llist.reverse2(llist.head)
#llist.reverse3()
print("\nreverse")
llist.reverseLLUsingStack()
llist.printList()
