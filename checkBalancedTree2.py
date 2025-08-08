#
# check balanced tree, all nodes have substrees with difference <= 1
#


class TreeUnbalanced(Exception):
    pass


# post order traversal, at each node compare the left and right subtrees height

class node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.lHeight = 0
        self.rHeight = 0
        self.parent = None



    def postTraverse(self):

        if node.left:
            self.lHeight = self.left.postTraverse()
        else:
            self.lHeight = 0

        if node.right:
            self.rHeight = self.right.postTraverse()
        else:
            self.rHeight = 0

        if abs(self.lHeight - self.rHeight) > 1:
            raise TreeUnbalanced()

        return (max(self.lHeight, self.rHeight) + 1)
        

    
