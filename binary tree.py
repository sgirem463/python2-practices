# binary search tree with list

class node:
    def __init__(self, value):
        self.value = value     # assume to be an integer for now
        self.left = -1         # the list index of the left child, initialized to -1
        self.right = -1        # the list index of the right child, initialized to -1


def insert(n, index, root): # insert node L[index] as root
    try:
        n
    except Exception as ex:
        print 'node not defined'
        print type(ex)
        raise
    
    print 'insert', n.value, index, root
    
    if (n.value < L[root].value):
        if (L[root].left == -1):
            L[root].left = index
            print 'left =', index
        else:
            insert(n, index, L[root].left)
    elif (n.value > L[root].value):
        if (L[root].right == -1):
            L[root].right = index
            print 'right =', index           
        else:
            insert(n, index, L[root].right)

def member(value, root): # return its index if member is in the tree, -1 if not
    try:
        root
    except Exception as ex:
        print 'root not defined'
        print type(ex)
        raise
    

    print 'member', value, root
    
    if (value == L[root].value):
        idx = root
    elif (value < L[root].value):
        if (L[root].left == -1):
            print 'left = -1'
            return -1
        else:
            idx = member(value, L[root].left)
    elif (value > L[root].value):
        if (L[root].right == -1):
            print 'right = -1'
            return -1
        else:
            idx = member(value, L[root].right)

    return idx

deleted = False

def delete(value, root): # delete item with value 'value' if exist, return index or -1
    global deleted
    
    if (root == -1):
        return -100 # not found

    # recursive
    if (value < L[root].value):
        r = delete(value, L[root].left)
        if (deleted): # if true, its left child is the node tree to be deleted
            if (L[L[root].left].left != -1):
                L[root].left = L[L[root].left].left
                L[root].value = L[L[root].left].value

            else:
                L[L[root].left] = -1
            deleted = False
        return r
    elif (value > L[root].value):
        r = delete(value, L[root].right)
        if (deleted): # if true, its right child is a one node tree to be deleted
            if (L[L[root].right].left != -1):
                L[root].right = L[L[root].left].left
                L[root].right = L[L[root].right].left

            else:
                L[root].right = -1
            deleted = False
        return r
    else: # found the value
        if (L[root].right != -1):
            v = deletemin(L[root].right)
            L[root].value = v            
            if (deleted): # its immediate right child is the minimul
                L[root].right = L[L[root].right].right
                deleted = False
            return 1
        elif (L[root].left != -1):
#            L[root].value = -1
            deleted = True
        else: # this node is a leaf
            L[root].value = -1
            deleted = True
            return 1
            

def deletemin(root): # delete the minimum item in tree
    global deleted
    
    # walk down the left child until it's NULL
    if (L[root].left == -1):
        # root is the minimal, its right child will take its position, mark 'deleted'
        # and let its (immediate) parent take care of the processing
        v = L[root].value
        L[root].value = -1
        deleted = True
        return v
    else:
        v = deletemin(L[root].left)
        if (deleted): # its left child is the minimum, relink the tree
            L[root].left = L[L[root].left].right
            deleted = False
        return v
        


def printTree(rootindex):
    if (rootindex == -1):
        return
    printTree(L[rootindex].left)
    print 'index:', rootindex, ' value:', L[rootindex].value, ' left:', L[rootindex].left, ' right:', L[rootindex].right
    printTree(L[rootindex].right)


def printList():
    for item in L:
        print 'L[', i, '] =', item.value, ' left =', item.left, ' right =', item.right

L = []
for i in [6, 1, 12, 4, 15, 9, 2, 8, 3, 11, 7]:
    n = node(i)
    L.append(n)
    insert(n, len(L) - 1, 0) # L[0] is the root, always true

# inorder traverse of the tree

printList()

print


printTree(0)

print

for j in [10, 3, 8, 15]:
    index = member(j, 0)
    print j, 'is at position:', index

# r = delete(9, 0)
# print 'delete:', r, 'deleted:', deleted
# printtree()

