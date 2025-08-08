import sets

'''
G = {}
G['a'] = []
G['b'] = []
G['c'] = []
G['d'] = []
G['e'] = []
G['f'] = []


G['g'] = []
G['h'] = []
G['i'] = []


G['a'].append('d')
G['f'].append('b')
G['b'].append('d')
G['f'].append('a')
G['d'].append('c')
'''


class graph:
    def __init__(self, v):
        self.node = v
        self.neighbors = []
        self.visited = False
        self.depth = 0


    def addNeighbor(self, node):
        self.neighbors.append(node)

a = graph('a')
b = graph('b')
c = graph('c')
d = graph('d')
e = graph('e')
f = graph('f')

a.addNeighbor(d)
f.addNeighbor(b)
b.addNeighbor(d)
f.addNeighbor(a)
d.addNeighbor(c)

V = {a,b,c,d,e,f}


print V

# S = set # starting nodes

# S = sets.Set(V)
S = {a,b,c,d,e,f}
print S

for v in V:
    for n in v.neighbors:
        print n
        if n in S:
            S.remove(n)


print 'S:', S

def dfs(current, depth):
    if current.visited:
        for x in current.neighbors:
            if x.depth < depth:
                print 'loop detected, failed'
                return False
        return True
    current.visited = True
    current.depth = depth
    print 'current:', current.node, 'depth:', current.depth

    for w in current.neighbors:
        r = dfs(w, depth + 1)
        if not r:
            return False
    return True

print 'S contents:'
for v in S:
    print v.node

def projectOrder():
    global V
    global S
    r = False
    
    if len(S) == 0:
        return False

    for v in S:
        r = dfs(v, 0)
    return r
    

answer = projectOrder()

print answer
