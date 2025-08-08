# tree implementation

class myTree:
    def __init__(self, node = None):
        self.root = None
        self.size = 0


    def insert(self, key):
        if not self.root:
            self.root = myTreeNode(key, parent = self.root)
            self.size += 1
        else:
            self._insert(self.root, key)

    def _insert(self, current, key):
        if (key < current.key):
            if not current.leftChild:
                current.leftChild = myTreeNode(key, parent = current)
#                current.rightChild.parent = current
                self.size += 1
            else:
                self._insert(current.leftChild, key)
        else: # key > or special case >= parent.key
            if not current.rightChild:
                current.rightChild = myTreeNode(key, parent = current)
#                current.rightChild.parent = current
                self.size += 1
            else:
                self._insert(current.rightChild, key)

    def find(self, key):
        print 'find:', key
        if not (self.root):
            return None
        else:
            return self._find(self.root, key)

    def _find(self, current, key):
        self._visitNode(current)
        if key == current.key:
            return key
        elif key < current.key:
            if current.leftChild:
                return self._find(current.leftChild, key)
            else:
                return None
        else: # key > current.key
            if current.rightChild:
                return self._find(current.rightChild, key)
            else:
                return None

    def treeSize(self):
        return self.size

    def _visitNode(self, node):
        print(node, ':', node.key)

    def inOrderTraverse(self):
        if not self.root:
            return
        else:
            self._inOrderTraverse(self.root)


    def _inOrderTraverse(self, current):
        if current.leftChild:
            self._inOrderTraverse(current.leftChild)
        self._visitNode(current)
        if current.rightChild:
            self._inOrderTraverse(current.rightChild)
           
    def preOrderTraverse(self):
        if not self.root:
            return
        else:
            self._preOrderTraverse(self.root)

    def _preOrderTraverse(self, current):
        self._visitNode(current)
        if current.leftChild:
            self._preOrderTraverse(current.leftChild)
        if current.rightChild:
            self._preOrderTraverse(current.rightChild)        

    def postOrderTraverse(self):
        if not self.root:
            return
        else:
            self._postOrderTraverse(self.root)

    def _postOrderTraverse(self, current):
        if current.leftChild:
            self._postOrderTraverse(current.leftChild)
        if current.rightChild:
            self._postOrderTraverse(current.rightChild)        
        self._visitNode(current)



class myTreeNode:
    def __init__(self, key, leftChild = None, rightChild = None, parent = None):
        self.key = key
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.parent = parent



tree = myTree()

tree.insert(11)
tree.insert(6)
tree.insert(15)
tree.insert(8)
tree.insert(13)
tree.insert(4)
tree.insert(19)
tree.insert(9)
tree.insert(12)
# tree.insert(7)
tree.insert(17)
tree.insert(5)
tree.insert(18)
tree.insert(1)
tree.insert(14)
tree.insert(3)
# tree.insert(16)
tree.insert(2)

'''

                                                  11
                          6                                               15
             4                         8                     13                         19
      1              5                        9        12          14           17
          3                                                                          18
        2


'''











tree.inOrderTraverse()
print

print tree.find(9)
print
print tree.find(16)
print
print tree.find(0)
print
print tree.find(15)
print
print tree.find(3)
print
print tree.find(1)
print
print tree.find(22)
print

print 'tree size:', tree.treeSize()
print

tree.preOrderTraverse()
print
tree.postOrderTraverse()

