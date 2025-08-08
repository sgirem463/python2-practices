# rank fro stream

import random
import sets


class treeNode:
    def __init__(self, key, size, left = None, right = None, parent = None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
        self.size = size

    def insert(self, key):
        if key < self.key:
            if self.left == None:
                self.left = treeNode(key, 1, parent = self)
            else:
                self.left.insert(key)
            self.size += 1
        else:
            if self.right == None:
                self.right = treeNode(key, 1, parent = self)
            else:
                self.right.insert(key)
            self.size += 1

    def find(self, key, rank):
        if key == self.key:
            if self.left:
                lSize = self.left.size
            else:
                lSize = 0
            return [key, rank + lSize + 1]
        if key < self.key:
            if self.left == None:
                return -1
            else:
                return self.left.find(key, rank)
        else:
            if self.right == None:
                return -1
            else:
                if self.left:
                    lSize = self.left.size
                else:
                    lSize = 0
                return self.right.find(key, rank + lSize + 1)


    def inOrderTraverse(self):
        if self.left:
            self.left.inOrderTraverse()
        print 'visit:', self.key, 'size:', self.size
        if self.right:
            self.right.inOrderTraverse()




A = list({random.randrange(100) for i in range(38)})
size = len(A)
print 'A size:', size
print
random.shuffle(A)
print A
print sorted(A)
print

root = treeNode(A[0], 1)

for i in range(1, size):
    root.insert(A[i])


root.inOrderTraverse()

print root.find(A[5], rank = 0)
print root.find(A[11], rank = 0)

print root.find(A[16], rank = 0)
print root.find(A[23], rank = 0)
