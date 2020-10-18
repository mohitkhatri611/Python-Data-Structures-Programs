class Node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.v=val


class Tree:
    def __init__(self):
        self.root=None

    def getRoot(self):
        return self.root

    def add(self,val):
        if self.root is None:
            self.root=Node(val)
        else:
            self._add(val,self.root)

    def _add(self,val,node):
        if val < node.v:
            if node.left is not None:
                self._add(val, node.left)
            else:
                node.left=Node(val)
        else:
            if node.right is not None:
                self._add(val,node.right)
            else:
                node.right=Node(val)

    def find(self,val):
        if self.root is not None:
            return self._find(val,self.root)

    def _find(self,val,node):
        if val==node.v:
            print('----------')
            print(' found the value')
        elif val < node.v and node.left is not None:
            self._find(val,node.left)
        elif val > node.v and node.right is not None:
            self._find(val, node.right)
        else:
            print('----------------')
            print('value not found')
    def deletTree(self):
        self.root=None
        print('--------')
        print('Tree deleted')

    def printTree(self):
        if self.root is not None:
            print('--------------')
            print(' Tree values are shown below:')
            self._printTree(self.root)
            print('-------')
    def _printTree(self,node):
        if node is not None:
            self._printTree(node.left)
            print('|       ',str(node.v), '         |')
            self._printTree(node.right)

tree=Tree()

while True:
    print("1. Add Elements\n 2. Search\n 3. Print Tree\n 4.Delete Tree and Exit\n")
    choice = int(input('Enter your choice: '))
    if choice==1:
        val=int(input('Enter the value:'))
        tree.add(val)
    elif choice==2:
        val=int(input('Enter the value to be Searched'))
        tree.find(val)
    elif choice==3:
        tree.printTree()
    elif choice==4:
        tree.deletTree()
        break
    else:
        print("wrong choice\n")