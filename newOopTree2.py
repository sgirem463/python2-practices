

class treeNode:
    def __init__(self, key, leftChild = None, rightChild = None, parent = None):
        self.key = key
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.parent = parent


    def _insert(self, key):
        if self.key == key:
           print key, 'already exists'
           return
        elif key < self.key:
            if not self.leftChild:
               self.leftChild = treeNode(key, parent = self)
            else:
               self.leftChild._insert(key)

        else:
            if not self.rightChild:
                self.rightChild = treeNode(key, parent = self)
            else:
                self.rightChild._insert(key)


    def _find(self, key):
        if key == self.key:
            print 'found', key
            return key
        elif key < self.key:
            if self.leftChild:
                self.leftChild._find(key)
            else:
                return None

        else:
            if self.rightChild:
                self.rightChild._find(key)
            else:
                return None            


    def visitNode(self):
        print 'visiting', self.key



    def inOrderTraverse(self):
        if self.leftChild:
            self.leftChild.inOrderTraverse()
        self.visitNode()
        if self.rightChild:
            self.rightChild.inOrderTraverse()        
        
    def preOrderTraverse(self):
        self.visitNode()
        if self.leftChild:
            self.leftChild.preOrderTraverse()
        if self.rightChild:
            self.rightChild.preOrderTraverse()      



        
    def postOrderTraverse(self):
        pass



tree = treeNode(11)

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


tree.inOrderTraverse()
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
tree.preOrderTraverse()

