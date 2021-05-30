#https://www.geeksforgeeks.org/linked-list-set-1-introduction/


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None


    def push(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode

    def insertAfter(self,prevNode,data):
        newNode=Node(data)

        if prevNode is None:
            print('prev node should be in lList')
            return
        newNode.next=prevNode.next
        prevNode.next=newNode

    def append(self,data):

        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            return

        last=self.head
        while last.next:
            last=last.next

        last.next=newNode




    def printList(self):
        temp=self.head
        while temp:
            print(temp.data,end=' ')
            temp=temp.next




if __name__=='__main__':
    # Start with the empty list
    llist = LinkedList()

    # Insert 6.  So linked list becomes 6->None
    llist.append(6)

    # Insert 7 at the beginning. So linked list becomes 7->6->None
    llist.push(7);

    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    llist.push(1);

    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    llist.append(4)

    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
    llist.insertAfter(llist.head.next, 8)
    print("Created linked list is:")
    print(llist.printList())