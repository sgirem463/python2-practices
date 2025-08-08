# array to minimum height binary tree

A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]


class treeNode:
    def __init__(self, key, left = None, right = None, parent = None):
        print 'new key:', key
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent



    def insertNode(self, key):
        print 'insert:', key
        if key < self.key:
            if self.left:
                self.left.insertNode(key)
            else:
                self.left = treeNode(key, parent = self)
        elif key > self.key:
            if self.right:
                self.right.insertNode(key)
            else:
                self.right = treeNode(key, parent = self)

    def inOrderTraverse(self):
        if self.left:
            self.left.inOrderTraverse()
        print 'visit:', self.key
        if self.right:
            self.right.inOrderTraverse()

    def buildMinTree(self, L):
        size = len(L)
        print 'size:', size
        if size == 1:
            self.insertNode(L[0])
            return
        
        if (size % 2 == 1):
            middle = size / 2 
        else:
            middle = size / 2 - 1
        self.insertNode(L[middle])
        if (middle > 0):
            self.buildMinTree(L[:middle])
        if (middle + 1 < size):
            self.buildMinTree(L[middle + 1 :])

        


size = len(A)
if (size % 2 == 1):
    middle = size / 2
else:
    middle = size / 2 - 1

tree = treeNode(A[middle])
tree.buildMinTree(A[:middle])
tree.buildMinTree(A[middle + 1 :])

tree.inOrderTraverse()

