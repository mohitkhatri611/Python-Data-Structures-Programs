# Python Program to calculate size of the tree iteratively
"""..............algo takes O(n) complexity ..............  """


# Node Structure
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# Return size of tree
def sizeoftree(root):
    if root == None:
        return 0
    q = []
    q.append(root)
    count = 1
    while (len(q) != 0):
        root = q.pop(0)
        if (root.left):
            q.append(root.left)
            count += 1
        if (root.right):
            q.append(root.right)
            count += 1
    return count


# Driver Program
root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
print(sizeoftree(root))

# This is code is contributed by simranjenny84
