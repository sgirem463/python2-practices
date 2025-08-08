# Python program to do inorder traversal without recursion
 
# A binary tree node
class Node:
     
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None
 
# Iterative function for inorder tree traversal
def inOrder(root):
     
    # Set current to root of binary tree
    current = root 
    s = [] # initialze stack
    s.append(current)
     
    while(len(s) > 0):

        if (current):
            current = current.left 
            
            # Place pointer to a tree node on the stack 
            # before traversing the node's left subtree
            if (current):
                s.append(current)
                continue

        current = s.pop()
        print current.data
        current = current.right
        if (current):
            s.append(current)
            

 
# Driver program to test above function
 
""" Constructed binary tree is
            1
          /   \
         2     3
       /  \
      4    5   """
 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
inOrder(root)
 
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
