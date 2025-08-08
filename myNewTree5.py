# tree implementation without tree class

class myTreeNode:
    size = 0
    def __init__(self, key, leftChild = None, rightChild = None, parent = None):
        self.key = key
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.parent = parent
        myTreeNode.size += 1

    def _insert(self, current, key):
        if (key < current.key):
            if not current.leftChild:
                current.leftChild = myTreeNode(key, parent = current)
            else:
                self._insert(current.leftChild, key)
        else: # key > or special case >= parent.key
            if not current.rightChild:
                current.rightChild = myTreeNode(key, parent = current)
            else:
                self._insert(current.rightChild, key)

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


    @classmethod
    def treeSize(cls):
        return cls.size

    def _visitNode(self, node):
        print(node, ':', node.key)

    def _inOrderTraverse(self, current):
        if current.leftChild:
            self._inOrderTraverse(current.leftChild)
        self._visitNode(current)
        if current.parent:
            print 'my parent:', current.parent.key
        else:
            print 'my parent:', current.parent
        if current.rightChild:
            self._inOrderTraverse(current.rightChild)

    def _preOrderTraverse(self, current):
        self._visitNode(current)
        if current.leftChild:
            self._preOrderTraverse(current.leftChild)
        if current.rightChild:
            self._preOrderTraverse(current.rightChild)        

    def _postOrderTraverse(self, current):
        if current.leftChild:
            self._postOrderTraverse(current.leftChild)
        if current.rightChild:
            self._postOrderTraverse(current.rightChild)        
        self._visitNode(current)



tree = myTreeNode(11)

tree._insert(tree, 6)
tree._insert(tree, 15)
tree._insert(tree, 8)
tree._insert(tree, 13)
tree._insert(tree, 4)
tree._insert(tree, 19)
tree._insert(tree, 9)
tree._insert(tree, 12)
# tree._insert(7)
tree._insert(tree, 17)
tree._insert(tree, 5)
tree._insert(tree, 18)
tree._insert(tree, 1)
tree._insert(tree, 14)
tree._insert(tree, 3)
# tree._insert(16)
tree._insert(tree, 2)

#
#
#                                                  11
#                          6                                               15
#             4                         8                     13                         19
#      1              5                        9        12          14           17
#          3                                                                          18
#        2
#


tree._inOrderTraverse(tree)
print

print tree._find(tree, 9)
print
print tree._find(tree, 16)
print
print tree._find(tree, 0)
print
print tree._find(tree, 15)
print
print tree._find(tree, 3)
print
print tree._find(tree, 1)
print
print tree._find(tree, 22)
print

print 'tree size:', myTreeNode.treeSize()
print

tree._preOrderTraverse(tree)
print
tree._postOrderTraverse(tree)

