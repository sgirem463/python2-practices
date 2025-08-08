# array to minimum height binary tree

A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]


class treeNode:
    def __init__(self, key, left = None, right = None, parent = None):
        print 'new key:', key
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent



    def insertNode(self, current, key):
        print 'insert:', key
        if key < current.key:
            if current.left:
                self.insertNode(current.left, key)
            else:
                current.left = treeNode(key, parent = current)
        elif key > current.key:
            if current.right:
                self.insertNode(current.right, key)
            else:
                current.right = treeNode(key, parent = current)

    def inOrderTraverse(self, current):
        if current.left:
            self.inOrderTraverse(current.left)
        print 'visit:', current.key
        if current.right:
            self.inOrderTraverse(current.right)

def buildMinTree(current, L):
    global tree
    size = len(L)
    print 'size:', size
    if size == 1:
        tree.insertNode(tree, L[0])
        return
        
    if (size % 2 == 1):
        middle = size / 2 
    else:
        middle = size / 2 - 1
    tree.insertNode(tree, L[middle])
    if (middle > 0):
        buildMinTree(tree, L[:middle])
    if (middle + 1 < size):
        buildMinTree(tree, L[middle + 1 :])

        


size = len(A)
if (size % 2 == 1):
    middle = size / 2
else:
    middle = size / 2 - 1

tree = treeNode(A[middle])
buildMinTree(tree, A[:middle])
buildMinTree(tree, A[middle + 1 :])

tree.inOrderTraverse(tree)
