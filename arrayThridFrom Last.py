#
# find the third from the last node in a linked list
#



class node:
    def __init__(self, value, nxt = None):
        self.value = value
        self.nxt = nxt


def thirdFromLast(h):

    if not h:
        return None
    if not h.nxt:
        return None
    if not h.nxt.nxt:
        return None

    p = h
    while True:
        if not p.nxt.nxt.nxt:
            return p
        else:
            p = p.nxt


def printList(H):
    p = H
    while(p):
        print p.value,
        p = p.nxt
    print



p = None
for i in range(10):
    n = node(i)
    if p:
        p.nxt = n
    else:
        Head = n
    p = n

printList(Head)


n = thirdFromLast(Head)
print n
print n.value
