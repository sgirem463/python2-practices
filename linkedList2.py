class node:
    def __init__(self, value):
        self.value = value
        self.next = None


    def add_node(self, value):
        a = node(value)
        a.next = self
        return a
        

head = node(3)

for i in [6,4,9,3,7,1]:
    head = head.add_node(i)
    

for i in [16,14,19,13,17,11]:
    head = head.add_node(i)

n = head

while n:
    print n.value
    n = n.next


