#Tree Traversal


class Node:
    def __init__(self, val):
        self.leftChild = None
        self.rightChild = None
        self.nodeData = val


#creating Instance of Node class to construct the tree

root = Node(1)
root.leftChild = Node(2)
root.rightChild = Node(3)
root.leftChild.leftChild = Node(4)
root.leftChild.rightChild = Node(5)


def InOrder(root):
    if root:
        InOrder(root.leftChild)
        print(root.nodeData)
        InOrder(root.rightChild)

def PreOrder(root):
    if root:
        print(root.nodeData)
        PreOrder(root.leftChild)
        PreOrder(root.rightChild)


def PostOrder(root):
    if root:
        PostOrder(root.leftChild)
        PostOrder(root.rightChild)
        print(root.nodeData)


def LevelOrder(root):
    pass



print("Pre Order Traversal:")
PreOrder(root)
print("In Order Traversal:")
InOrder(root)
print("Post Order Traversal:")
PostOrder(root)