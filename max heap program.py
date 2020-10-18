#https://www.geeksforgeeks.org/max-heap-in-python/?ref=leftbar-rightbar

import sys

class MaxHeap:
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.size=0
        self.Heap=[0]*(self.maxsize+1)
        self.Heap[0]=sys.maxsize
        self.FRONT=1


    def parent(self,pos):
        return pos//2

