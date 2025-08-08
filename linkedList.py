class node:
    last = None
    def __init__(self, value):
        self.value = value
        self.next = None
        if node.last == None:
            node.last = self


    def add_node_at_end(self, value):
        a = node(value)
        node.last.next = a
        node.last = a

    def printList(self):
        n = self
        while n:
            print n.value
            n = n.next
        


def printList(n):
    while n:
        print n.value
        n = n.next

# reverse the linked list
def reverseList(L):

    prev = None
    p = L

    while p:
        nex = p.next
        p.next = prev
        prev = p
        p = nex

    return prev


# reverse the first n items of the list
def reversePartial(L, n):
    prev = None
    head = L
    p = L

    while p and n:
        nex = p.next
        p.next = prev
        prev = p
        p = nex
        n -= 1

    if n > 0:
        return None
    else:
        head.next = p

    return prev
    
    

head = node(0)
for i in [2,4,6,8,10,12,14,16,18,20,22,24]:
    head.add_node_at_end(i)

print

head.printList()

print
n = head

while n:
    print n.value
    n = n.next


print
print

newHead = reverseList(head)

printList(newHead)
print
newHead.printList()

print
newHead = reversePartial(newHead, 5)
    
newHead.printList()
