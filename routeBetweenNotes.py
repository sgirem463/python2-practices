# find route between two nodes a and x


G = {'a': ['b', 'c', 'f'], 'b': ['f', 'g', 'k'], 'c': ['f', 'e', 'h'], 'd': ['h', 'i'], 'e': ['m', 's']}


def search1 (x, y):
    print 'visit:', x
    if x == y:
        print 'found:', x
        return True
    if x not in G:
        return
    root = x
    
    for w in G[root]:
        if w == y:
            print 'found:', w
            return True
        r = search1(w, y)
        if r == True:
            return r
        

print search1('a', 'c')
print search1('a', 'k')
print search1('a', 's')
print search1('a', 'i')



class node:
    def __init__(self, node):
        self.node = node
        self.visited = False
        self.neighbors = []
    def addNeighbors(self, nList):
        self.neighbors = nList

a = node('a')
b = node('b')
c = node('c')
d = node('d')
e = node('e')
f = node('f')
g = node('g')
h = node('h')
i = node('i')
j = node('j')
k = node('k')
l = node('l')
m = node('m')
n = node('n')
s = node('s')


a.addNeighbors([b, c, f])
b.addNeighbors([f, g, k])
c.addNeighbors([f, e, h])
d.addNeighbors([h, i])
e.addNeighbors([m, s])





def search(x, y):
    print 'visit:', x.node
    x.visited = True
    if x == y:
        print 'found:', x.node
        return True
    for w in x.neighbors:
        if not w.visited:
            r = search(w, y)
            if r:
                return r
    return False

print
print

print search(a, c)

for v in [a,b,c,d,e,f,g,h,i,j,k,l,m,n,s]:
    v.visited = False

print search(a, k)

for v in [a,b,c,d,e,f,g,h,i,j,k,l,m,n,s]:
    v.visited = False
    
print search(a, s)

for v in [a,b,c,d,e,f,g,h,i,j,k,l,m,n,s]:
    v.visited = False
    
print search(a, i)




