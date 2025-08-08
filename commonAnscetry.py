

class treeNode:
    def __init__(self, key, left = None, right = None, parent = None):
        # print 'new key:', key
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent



    def insertNode(self, key):
        # print 'insert:', key
        if key < self.key:
            if self.left:
                self.left.insertNode(key)
            else:
                self.left = treeNode(key, parent = self)
        elif key > self.key:
            if self.right:
                self.right.insertNode(key)
            else:
                self.right = treeNode(key, parent = self)




def search(root, x, Ancestor):
    # depth first search
    if root.key == x:
        Ancestor.append(x)
        return Ancestor

    if (not root.left) and (not root.right): # leave
        return None
    if root.left:
        r = search(root.left, x, Ancestor + [root.key])
        if r != None:
            return r
    if root.right:
        r = search(root.right, x, Ancestor + [root.key])
        if r != None:
            return r

    return None
        

def commonAnscetor(root, a, b):
    L1 = search(root, a, [])
    L2 = search(root, b, [])

    print a, 'anscetor path', L1
    print b, 'anscetor path', L2
    mm = max(len(L1), len(L2))
    for i in range (mm):
        if (i + 1) > len(L1) or (i + 1)  > len(L2):
            print a, b, 'common anscetor is:', L1[i-1]
            print
            return
        if L1[i] != L2[i]:
            print a, b, 'common anscetor is:', L1[i-1]
            print
            return


tree = treeNode(9)
tree.insertNode(6)
tree.insertNode(4)
tree.insertNode(1)
tree.insertNode(7)
tree.insertNode(12)
tree.insertNode(13)
tree.insertNode(10)
tree.insertNode(15)


commonAnscetor(tree, 4, 7)
commonAnscetor(tree, 1, 7)
commonAnscetor(tree, 7, 10)
commonAnscetor(tree, 10, 15)
commonAnscetor(tree, 4, 6)



