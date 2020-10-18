class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data=data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node=new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head=head

    def insert(self, data):
        new_node=Node(data)
        new_node.set_next(self.head)
        self.head=new_node

    def size(self):
        current =self.head
        count=0
        while current:
            count+=1
            print(current.get_data())
            current= current.get_next()
        print("The size of linked list is " ,count)

    def search(self, data):
        current=self.head
        found=False
        while current and found is False:
            if current.get_data() ==data:
                found=True
            else:
                current=current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return found

    def delete(self, data):
        current =self.head
        previous=None
        found=False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous=current
                current=current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head=current.get_next()
        else:
            previous.set_next(current.get_next())

l1=LinkedList()
l1.insert(1)
l1.insert(2)
l1.insert(3)
l1.size()

val=l1.search(1)
if val:
    print("value is found", val)
l1.delete(2)
#l1.delete(2)
l1.size()
