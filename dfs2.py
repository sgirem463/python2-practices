#
#
# deep first search
#

# start with S
#

import sys

class node():
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.children = []



n0 = node(0)
n1 = node(1)
n5 = node(5)
n4 = node(4)
n2 = node(2)
n3 = node(3)

n0.children.append(n1)
n0.children.append(n4)
n0.children.append(n5)
n1.children.append(n3)
n1.children.append(n4)
n2.children.append(n1)
n3.children.append(n2)
n3.children.append(n4)


S = n0

def dfs(node):
    if node.visited != True:
        node.visited = True
        print 'visit', node.value
        for c in node.children:
            if c.visited != True:
                dfs(c)

def visit2(n):
    n.visited = True
    print 'visit', n.value


def dfs2(node):
        visit2(node)
        for c in node.children:
            if not c.visited:
                dfs(c)
        


print 'DFS2'
dfs2(S)

sys.exit()


print 'DFS'
dfs(S)
print
print


queue = []
def bfs0(node):
    
    if node.visited != True:
        queue.insert(0, node)

    n = queue.pop()
    while not n.visited:
        n.visit = True
        print 'visit', n.value
        for p in n.children:
            if not p.visited:
                queue.insert(0, p)
        n = queue.pop()
        dfs(n)




n0 = node(0)
n1 = node(1)
n5 = node(5)
n4 = node(4)
n2 = node(2)
n3 = node(3)

n0.children.append(n1)
n0.children.append(n4)
n0.children.append(n5)
n1.children.append(n3)
n1.children.append(n4)
n2.children.append(n1)
n3.children.append(n2)
n3.children.append(n4)


S = n0


print

def visit(n):
    n.visited = True
    print 'visit', n.value
    
def bfs(root):
    queue = []
    visit(root)
    queue.insert(0, root)

    while len(queue) > 0:
        n = queue.pop()
        for c in n.children:
            if not c.visited:
                visit(c)
                queue.insert(0, c)

def visit3(n):
    print 'visit', n.value
    



def bfs3(root):
    queue = []
    root.visited = True
    queue.insert(0, root)

    while len(queue) > 0:
        n = queue.pop()
        visit3(n)
        for c in n.children:
            if not c.visited:
                c.visited = True
                queue.insert(0, c)


print
print



               
bfs3(S)               
