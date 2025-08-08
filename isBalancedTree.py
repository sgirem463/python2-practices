A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]


class treeNode:
    def __init__(self, key, left = None, right = None, parent = None):
        print 'new key:', key
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
        self.visited = False
#        self.level = level



    def insertNode(self, current, key):
#        print 'insert:', key
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


    

def dfs(current, level):
    global L
    current.visited = True
    print current.key
    L[level].append(current)
    if current.left:
        dfs(current.left, level = level + 1)
    if current.right:
        dfs(current.right, level = level + 1)
        
L = []
for i in range(100):
    L.append([])


dfs(tree, level = 0)

print
print
for i in range(100):
    if len(L[i]):
#        for j in range(len(L[i])):
#            print L[i][j].key,
#        print
            
        print([L[i][j].key for j in range(len(L[i]))])
    else:
        break


def checkBalance(current):
    if current.left:
        lDepth = checkBalance(current.left)
    else:
        lDepth = 0
    if current.right:
        rDepth = checkBalance(current.right)
    else:
        rDepth = 0
    print 'visit:', current.key
    if abs(lDepth - rDepth) > 1:
        print 'not balanced, current:', current.key, 'left:', current.left, 'right:', current.right
        return max(lDepth, rDepth) + 1
    else:
        return max(lDepth, rDepth) + 1

print
print 'check balanced'
print 'tree depth:', checkBalance(tree)




tree2 = treeNode(5)
tree.insertNode(tree2, 2)
tree.insertNode(tree2, 1)
tree.insertNode(tree2, 8)
print 'check balanced'

checkBalance(tree2)

tree.insertNode(tree2, 15)
tree.insertNode(tree2, 16)
tree.insertNode(tree2, 17)
print 'check balanced'
checkBalance(tree2)

'''
tree.insertNode(tree, 2)
tree.insertNode(tree, 2)
tree.insertNode(tree, 2)

'''


