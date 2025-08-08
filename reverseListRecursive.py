#
# reverse a linked list using a recursive algorithm
#

class node:
    def __init__(self, value, nxt = None):
        self.value = value
        self.nxt = nxt

head = None

def reverseList(L, p):
    global head
#    if p == NULL:
#        L[0].nxt = NULL
#    else:
#        L[0].nxt = P

    if L.nxt == None:
        head = L
        L.nxt = p
    else:
        nxt = L.nxt
        L.nxt = p
        reverseList(nxt, L)
        

L = None
p = None
for i in range(10):
    n = node(i)
    if L == None:
        L = n
    if p != None:
       p.nxt = n
    p = n

head = L
       
p = head
while p != None:
    print p.value
    p = p.nxt
    

reverseList(L, None)

print
p = head
while p != None:
    print p.value
    p = p.nxt
