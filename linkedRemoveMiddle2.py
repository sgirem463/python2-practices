#
# linked list, delete the middle node
#
import random

class node():

    def __init__(self, value):
        self.value = value
        self.next = None




size = random.randrange(10, 20)
print size


v = random.randrange(100)
print v,
L = node(v)
p = L


for i in range(size):
    v = random.randrange(100)
    print v,
    n = node(v)
    p.next = n
    p = n


print
p = L

while p != None:
    print p.value,
    p = p.next


#
# p goes down one node at a time
# p2 goes down two nodes at a time
#

p = L
p2 = L

# if p:
#    p2 = p.next

prev = None

while p2 != None:
    prev = p
    p = p.next
    if p2.next != None:
        p2 = p2.next.next
    else:
        p2 = None

print
print 'the middle value:', p.value

if prev:
    prev.next = p.next

print

p = L
while p != None:
    print p.value,
    p = p.next


