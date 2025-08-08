# build heap with tree nodes
'''

index 0 based
for parent at index n
leftChild : 2n + 1
rightChild : 2n + 2

for child at index n
parent = (n - 1) / 2   # integer division, or taking the floor of the division result


'''

import random
import sets


class treeNode:
    heapsize = 0
    lastNode = None
    def __init__(self, key, left = None, right = None, parent = None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
        treeNode.heapsize += 1


    def inOrderTraverse(self):
        if self.left:
            self.left.inOrderTraverse()
        print 'visit:', self.key
        if self.right:
            self.right.inOrderTraverse()

    def postOrderTraverse(self):
        if self.left:
            self.left.postOrderTraverse()
        if self.right:
            self.right.postOrderTraverse()
        print 'visit:', self.key
        
    def preOrderTraverse(self):
        if self.left:
            self.left.preOrderTraverse()
        if self.right:
            self.right.preOrderTraverse()
        print 'visit:', self.key


    def insert(self, key, path):

        if len(path) == 1:
            if self.left:
                self.right = treeNode(key, parent = self)
                self.right.shiftUp()

            else:
                self.left = treeNode(key, parent = self)
                self.left.shiftUp()

        elif path[1] == (path[0] * 2 + 1):
            self.left.insert(key, path[1:])
        else:
            self.right.insert(key, path[1:])

    def findLast(self, path):
        if len(path) == 1:
            if self.right:
                return self.right
            else:
                return self.left

        elif path[1] == (path[0] * 2 + 1):
            return self.left.findLast(path[1:])
        else:
            return self.right.findLast(path[1:])


    def shiftUp(self):
        if not self.parent:
            return

        if self.key < self.parent.key:
            tmp = self.key
            self.key = self.parent.key
            self.parent.key = tmp
            self.parent.shiftUp()
            

    def shiftDown(self):
        smallest = self
        if self.left:
            if self.left.key < self.key:
                smallest = self.left
        if self.right:
            if self.right.key < smallest.key:
                smallest = self.right
        if smallest != self:
            tmp = smallest.key
            smallest.key = self.key
            self.key = tmp
            smallest.shiftDown()
            
    def swapKey(self, a, b):
        tmp = a.key
        a.key = b.key
        b.key = tmp
        
    def getMin(self):
        r = self.key
        if self.heapsize == 1:
            self = None
            return r
        path = getPath(self.heapsize - 1)
        last = self.findLast(path)
        self.swapKey(self, last)
        if last.parent.left == last:
            last.parent.left = None
        else:
            last.parent.right = None
        treeNode.heapsize -= 1
        self.shiftDown()
        return r
        


    def bfs(self):
        queue = []
        if self:
            queue.append(self)
        while len(queue) > 0:
            node = queue.pop()
            print 'visit:', node.key
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            

    def dfs(self, level):
        global L
        self.visited = True
        print self.key
        L[level].append(self)
        if self.left:
            self.left.dfs(level = level + 1)
        if self.right:
            self.right.dfs(level = level + 1)


def getPath(size):
        n = size
        path = []
        while n > 0:
            n = (n - 1) / 2
            path.append(n)
        path.reverse()
        print 'path:', path
        return path



A = list({random.randrange(100) for i in range(38)})
size = len(A)
print 'A size:', size
print
random.shuffle(A)
print A
print sorted(A)
print
path = getPath(size)
print 'path:', path
print

if size > 0:
    root = treeNode(A[0])
    treeNode.lastNode = root
    
for i in range(1, size):
    root.insert(A[i], getPath(root.heapsize))



        
L = []
for i in range(20):
    L.append([])


root.dfs(level = 0)

print
print
for i in range(20):
    if len(L[i]):
#        for j in range(len(L[i])):
#            print L[i][j].key,
#        print
            
        print([L[i][j].key for j in range(len(L[i]))])
    else:
        break

'''
print
root.inOrderTraverse()
print

print
root.postOrderTraverse()
print

print
root.preOrderTraverse()
print
'''


print
root.bfs()
print

for i in range(size):
    print root.getMin()


print
print 'traverse tree again'
root.inOrderTraverse()
print

        
L = []
for i in range(20):
    L.append([])


dfs(root, level = 0)

print
print
for i in range(20):
    if len(L[i]):
#        for j in range(len(L[i])):
#            print L[i][j].key,
#        print
            
        print([L[i][j].key for j in range(len(L[i]))])
    else:
        break
