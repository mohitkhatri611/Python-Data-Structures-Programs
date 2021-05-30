# for Garbage collection
import gc
class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None


class DoublyLinkedList:

    def __init__(self):
        self.head=None
    def push(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return

        newNode.next=self.head
        self.head.prev=newNode
        self.head=newNode

    def insertBefore(head_ref, next_node, new_data):

        # /*1. check if the given next_node is NULL */
        if (next_node == None):
            print("the given next node cannot be NULL")
            return

        # /* 3. put in the data */
        new_node = Node(new_data)

        # /* 4. Make prev of new node as prev of next_node */
        new_node.prev = next_node.prev

        # /* 5. Make the prev of next_node as new_node */
        next_node.prev = new_node

        # /* 6. Make next_node as next of new_node */
        new_node.next = next_node

        # /* 7. Change next of new_node's previous node */
        if (new_node.prev != None):
            new_node.prev.next = new_node

        # /* 8. If the prev of new_node is NULL, it will be
        #   the new head node */
        else:
            head_ref = new_node


    def insertAfter(self,prev_node,data):
        if prev_node is None:
            print("the given positon can't be null")
            return

        new_node=Node(data)

        new_node.next=prev_node.next
        new_node.prev = prev_node

        prev_node.next=new_node
        if new_node.next:
            new_node.next.prev=new_node



    def append(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            return
        last =self.head
        while last .next:
            last =last .next
        last .next=newNode
        newNode.prev = last
        #last .next.prev=last

    def deleteNode(self, dele):
        #delete a given node in a doubly linked list.
        # Base Case
        if self.head is None or dele is None:
            return

        # If node to be deleted is head node
        if self.head == dele:
            self.head = dele.next

        # Change next only if node to be deleted is NOT
        # the last node
        if dele.next is not None:
            dele.next.prev = dele.prev

        # Change prev only if node to be deleted is NOT
        # the first node
        if dele.prev is not None:
            dele.prev.next = dele.next
        # Finally, free the memory occupied by dele
        # Call python garbage collector
        gc.collect()

    def deleteNode2(self,head_ref, del_):

        # base case
        if (head_ref == None or del_ == None):
            return

        # If node to be deleted is head node
        if (head_ref == del_):
            head_ref = del_.next

        # Change next only if node to be deleted is NOT
        # the last node
        if (del_.next != None):
            del_.next.prev = del_.prev

        # Change prev only if node to be deleted is NOT
        # the first node
        if (del_.prev != None):
            del_.prev.next = del_.next

        return head_ref
    def deleteNodeAtGivenPos(self,head_ref, n):

        # if list in None or invalid position is given
        if (head_ref == None or n <= 0):
            return

        current = head_ref
        i = 1

        # traverse up to the node at position 'n' from
        # the beginning
        while (current != None and i < n):
            current = current.next
            i = i + 1

        # if 'n' is greater than the number of nodes
        # in the doubly linked list
        if (current == None):
            return

        # delete the node pointed to by 'current'
        self.deleteNode2(head_ref, current)

        return head_ref

    def printDL(self):
        temp=self.head

        while temp:
            print(temp.data, end=" ")
            temp=temp.next


if __name__=="__main__":

    llist = DoublyLinkedList()
    llist.append(1)
    llist.append(6)
    llist.append(0)
    llist.push(3)
    llist.push(7)
    llist.insertAfter(llist.head.next.next, 8)
    print("before deletion")
    llist.printDL()
    print("\n after del")
    #here position are starting with 1 of 1st index
    head = llist.deleteNodeAtGivenPos(llist.head, 2)

    llist.printDL()
