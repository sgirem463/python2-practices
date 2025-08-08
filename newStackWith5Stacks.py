# one stack implemented with multiple stacks

class newStack:
    def __init__(self):
        self.stacks = [[],[],[],[],[],[]]
        self.nItems = 0
        self.cStack = 0  # current stck from 0 to 4
    def pop(self):
        if self.nItems == 0:
            print 'stack empty'
            return
        cStack = (self.nItems - 1) / 5 # each internal stack can hold 5 items
        item = self.stacks[cStack].pop()
        self.nItems -= 1
        print self.stacks
        return item
    def push(self, n):
        if self.nItems == 25:
            print 'stack full'
            return
        cStack = (self.nItems) / 5 # each internal stack can hold 5 items
        self.stacks[cStack].append(n)
        self.nItems += 1
        print self.stacks


s = newStack()

print s.pop()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.push(7)
s.push(8)
s.push(9)
s.push(10)
s.push(11)
s.push(12)
s.push(13)
s.push(14)
s.push(15)
s.push(16)
print s.pop()
s.push(17)
s.push(18)
s.push(19)
s.push(20)
s.push(21)
s.push(22)
s.push(23)
s.push(24)
s.push(25)
s.push(26)
s.push(27)

print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()


