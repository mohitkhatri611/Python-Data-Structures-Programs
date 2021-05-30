# A complete working Python3 program to
# demonstrate deletion in singly
# linked list with class

# Node class
class Node:


    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def deleteNode(self, key):
        temp=self.head
        prev=temp

        if temp is not None:
            if temp.data==key:
                self.head=temp.next
                temp=None
                return

            while temp is not None:
                if temp.data==key:
                    break
                prev=temp
                temp=temp.next

            if temp==None:
                return

            prev.next=temp.next
            temp=None
    def delNode2(self, position):
        if self.head==None:
            return
        temp = self.head

        if position ==0:
            self.head=temp.next
            temp=None
            return
        for i in range(position -1):
            temp= temp.next
            if temp is None:
                break

        if temp is None:
            return
        if temp.next is None:
            return
        prev=temp.next.next
        temp.next=None
        temp.next=prev
    def delNode3(self,pos):
        #other way to delete pos.
        temp = Node(0)
        temp.next = self.head
        prev = temp
        count = -1
        curr = self.head
        while curr:
            count += 1
            if count == pos:
                r = curr
                prev.next = curr.next
                r.next = None
                break
            prev = curr
            curr = curr.next
        return temp.next
    def getCountRec(self,node):
        if node is None:
            return 0
        else:
            return 1+ self.getCountRec(node.next)

    def getCount(self):
        #counted nodes witout recursion
        return self.getCountRec(self.head)

    def getCount2(self):
        #using without recursion
        temp= self.head
        count=0

        while temp:
            count+=1
            temp=temp.next
        return count
    def printList(self):
        temp = self.head
        while (temp):
            print(" %d" % (temp.data), end=' '),
            temp = temp.next

    def search(self,li,key):
        if not li:
            return False
        if li.data==key:
            return True,key
        return self.search(li.next,key)




# Driver program
llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
llist.push(8)


print("Created Linked List: ")
llist.printList()
print("total nodes before deletiong",llist.getCount())

llist.delNode3(4)

print("\nLinked List after Deletion of 1:")
llist.printList()
print("total nodes",llist.getCount2())

print("search key is there", llist.search(llist.head,3))