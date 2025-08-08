#
# check if a binary tree is a binary search tree
#

# in order traverse, check if the output is ascending
#

class NotBstException(Exception):
    pass


    def inOrderTraverse(self):
        if self.left:
            lValue = self.left.inOrderTraverse()
        print self.value

        if lValue > self.value:
            raise NotBstException()
        
        if self.right:
            rValue = self.right.inOrderTraverse()
            
        if rValue < self.value:
            raise NotBstException()
            
        return self.value



