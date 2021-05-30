"""2ways first second is taking O(n^2) and firstone is  using queue is taking o(n)"""








class Node:
    def __init__(self,data):
        self.data= data
        self.left=None
        self.right=None

"""this will take O(n)"""
class level1:
    def printLevelOrder(self,root):

        if root is None:
            return
        queue=[]

        queue.append(root)
        print("printing using only O(n) algo queue:")
        while(len(queue)>0):
            print(queue)
            print(queue[0].data, end=' ')
            node=queue.pop(0)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)


"""second: --the below code is taking O(n^2) time if tree is sked and space is o(n) for workst skew other wise log(n)"""
class level:
    def printLevelOrder(self,root):
        h=self.height2(root)
        for i in range(1,h+1):
            self.printCurrentLevel(root,i)


    def printCurrentLevel(self,root , level):
        if root is None:
            return
        if level == 1:
            print(root.data,end=" ")
        elif level > 1 :
            self.printCurrentLevel(root.left , level-1)
            self.printCurrentLevel(root.right , level-1)

    #this height will be counting root as 0
    def height(self,node1):
        if node1 is None:
            return 0
        elif node1.left is None and node1.right is None:
            return 0 #return 1 if this height is counting to 0 as root
        else:
            return 1 +  (max(self.height(node1.left),self.height(node1.right)))

    #this height is takign root as 1 count like level
    def height2(self,node):
        if node is None:
            return 0
        else:
            # Compute the height of each subtree
            lheight = self.height2(node.left)
            rheight = self.height2(node.right)

            # Use the larger one
            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1


if __name__=="__main__":

    root = Node(1)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(4)
    root.left.right = Node(3)

    lev1 = level1()
    lev1.printLevelOrder(root)
    # lev=level()
    # print(lev.height2(root))
    # lev.printLevelOrder(root)
