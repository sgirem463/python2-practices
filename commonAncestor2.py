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



    def insertNode(self, current, key):
        if key < current.key:
            if not current.left:
                current.left = treeNode(key, parent = current)
            else:
                self.insertNode(current.left, key)
        if key > current.key:
            if not current.right:
                current.right = treeNode(key, parent = current)
            else:
                self.insertNode(current.right, key)


    def inOrderTraverse(self, current):
        if current.left:
            self.inOrderTraverse(current.left)
        print 'visit:', current, 'key:', current.key
        if current.right:
            self.inOrderTraverse(current.right)           
                


    def findKey(self, current, key):
        if current.key == key:
            print 'found:', current.key
            return current
        if current.left:
            r = self.findKey(current.left, key)
            if r:
                return r
        if current.right:
            r = self.findKey(current.right, key)
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

p = tree.findKey(tree, 2)
print p
if p:
    print p.key
q = tree.findKey(tree, 19)
print q
if q:
    print q.key

print
print 'find common anscetor:'
findCommonAnscetor(p, q)


p = tree.findKey(tree, 15)
print p
if p:
    print p.key
q = tree.findKey(tree, 21)
print q
if q:
    print q.key

print
print 'find common anscetor:'
findCommonAnscetor(p, q)
