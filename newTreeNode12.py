# tree

class myTreeNode:
    size = 0
    def __init__(self, key, leftChild = None, rightChild = None, parent = None):
        self.key = key
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.parent = parent
        myTreeNode.size += 1

    def _insert(self, key):
        if key < self.key:
            if not self.leftChild:
                self.leftChild = myTreeNode(key, parent = self)
            else:
                self.leftChild._insert( key)
        else:
            if not self.rightChild:
                self.rightChild = myTreeNode(key, parent = self)
            else:
                self.rightChild._insert( key)

    def _find(self, key):
        self._visitNode()
        if key == self.key:
            return key
        elif key < self.key:
            if self.leftChild:
                return self.leftChild._find(key)
            else:
                return None

        else:
            if self.rightChild:
                return self.rightChild._find( key)
            else:
                return None

    def _visitNode(self):
        print(self, ':', self.key)



tree = myTreeNode(11)

tree._insert(6)
tree._insert(15)
tree._insert(8)
tree._insert(13)
tree._insert(4)
tree._insert(19)
tree._insert(9)
tree._insert(12)
# tree._insert(7)
tree._insert(17)
tree._insert(5)
tree._insert(8)
tree._insert(1)
tree._insert(14)
tree._insert(3)
# tree._insert(16)
tree._insert(2)

#
#
#                                                  11
#                          6                                               15
#             4                         8                     13                         19
#      1              5                        9        12          14           17
#          3                                                                          18
#        2
#


#tree._inOrderTraverse(tree)
print

print tree._find(9)
print
print tree._find(16)
print
print tree._find(0)
print
print tree._find(15)
print
print tree._find(3)
print
print tree._find(1)
print
print tree._find(22)
print
