#
# linked list removeDups
#

import random

class node():
    def __init__(self, value):
        self.value = value
        self.next = None
        



def removeDups(L):





    
    pass



#
# L is the head of the list
#
v = random.randrange(10)
print v,
L = node(v)
p = L

for i in range(20):
    v = random.randrange(10)
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
# p is the current node, check all subsequent nodes
# move p to the next
#

p = L

while p != None:
    v = p.value
    prev = p
    q = p.next
    while q != None:
        if q.value == v:
            prev.next = q.next
            q = q.next
            # prev remains the same
        else:
            prev = q
            q = q.next
    p = p.next


print
p = L

        
while p != None:
    print p.value,
    p = p.next

    
    
    

