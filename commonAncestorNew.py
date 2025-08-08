# common ancestor

A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]

p = None
q = None

class treeNode:
    def __init__(self, key, parent = None):
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None
        self.visited = False
        self.ancestor = False



    def insertNode(self, key):
        if key < self.key:
            if not self.left:
                self.left = treeNode(key, parent = self)
            else:
                self.left.insertNode(key)
        if key > self.key:
            if not self.right:
                self.right = treeNode(key, parent = self)
            else:
                self.right.insertNode(key)


    def inOrderTraverse(self):
        if self.left:
            self.left.inOrderTraverse()
        print 'visit:', self, 'key:', self.key
        if self.right:
            self.right.inOrderTraverse()           
                

    def preOrderTraverse(self):
        print 'visit:', self, 'key:', self.key
        if self.left:
            self.left.preOrderTraverse()
        if self.right:
            self.right.preOrderTraverse()

    def postOrderTraverse(self):
        if self.left:
            self.left.postOrderTraverse()
        if self.right:
            self.right.postOrderTraverse()
        print 'visit:', self, 'key:', self.key


    def findKey(self, key):
        if self.key == key:
            print 'found:', self.key
            return self
        else:
            print 'visited', self.key
        if self.left:
            r = self.left.findKey(key)
            if r:
                return r
        if self.right:
            r = self.right.findKey(key)
            if r:
                return r
        return None
            
        
def findCommonAnscetor(p, q):
    while (p):
        p.ancestor = True
        p = p.parent

    while (q):
        if q.ancestor:
            print 'found:', q, 'key', q.key
            return q
        q = q.parent
    print 'not found'
    return None


    

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
    tree.insertNode(L[middle])
    if (middle > 0):
        buildMinTree(tree, L[:middle])
    if (middle + 1 < size):
        buildMinTree(tree, L[middle + 1 :])


def buildMinTree2(tree, L):
    size = len(L)
    print 'size:', size
#    if size == 1:
#        tree.insertNode(L[0])
#        return
        
    if (size % 2 == 1):
        middle = size / 2 
    else:
        middle = size / 2 - 1
    tree.insertNode(L[middle])
    if (middle > 0):
        buildMinTree2(tree, L[:middle])
    if (middle + 1 < size):
        buildMinTree2(tree, L[middle + 1 :])


def buildTree(root, key):
    if not root:
        root = treeNode(key, parent = None)
    else:
        root.insertNode(key)
    return root


def buildTree2(root, key):
    try:
        root
    except NameError:
        root = treeNode(key, parent = None)
    else:
        root.insertNode(key)







size = len(A)
if (size % 2 == 1):
    middle = size / 2
else:
    middle = size / 2 - 1

tree = treeNode(A[middle])
buildMinTree2(tree, A[:middle])
buildMinTree2(tree, A[middle + 1 :])

print
print 'inOrderTraverse....'
tree.inOrderTraverse()
print

print 'preOrderTraverse....'
tree.preOrderTraverse()
print

print 'postOrderTraverse....'
tree.postOrderTraverse()

print

p = tree.findKey(2)
print p
if p:
    print p.key
q = tree.findKey(19)
print q
if q:
    print q.key

q = tree.findKey(50)
print q
if q:
    print q.key
else:
    print 'not found'

print
print 'find common anscetor:'
findCommonAnscetor(p, q)


p = tree.findKey(15)
print p
if p:
    print p.key
q = tree.findKey(21)
print q
if q:
    print q.key

print
print 'find common anscetor:'
findCommonAnscetor(p, q)


import random

K = []

for i in range(23):
	n = random.randrange(100)
	if n not in K:
	    K.append(n)

print
print K

tree2 = None
for i in K:
    tree2 = buildTree(tree2, i)


print
print 'new inOrderTraverse....'
tree2.inOrderTraverse()

for i in K:
    tree3 = buildTree2(tree3, i)

print 'new preOrderTraverse....'
tree3.preOrderTraverse()


