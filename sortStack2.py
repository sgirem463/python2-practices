#
# sort stack
#
# push, pop, peek, isEmpty
#

class sortStack():
    def __init__(self):
        self.stack = []
        self.tmpStack = []
        

    def push(self, value):
            
        while True:
            if self.isEmpty():
                self.stack.append(value)
                while len(self.tmpStack) > 0:
                    self.stack.append(self.tmpStack.pop())
                break
            elif self.peek() < value:
                self.tmpStack.append(self.stack.pop())
            else:
                self.stack.append(value)
                while len(self.tmpStack) > 0:
                    self.stack.append(self.tmpStack.pop())
                break
                    

    def pop(self):
        try:
            value = self.stack.pop()
            return value
        except Exception as ex:
            print ex
            return None


    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.stack[len(self.stack) - 1]

    def isEmpty(self):
        return (len(self.stack) == 0)

    def sprint(self):
        print self.stack[::-1]
        

s = sortStack()

print s.pop()
s.push(8)
s.push(1)
s.push(9)
s.push(4)
s.push(5)
s.sprint()
s.push(2)
s.push(7)
s.push(6)
s.push(3)
print s.pop()

s.push(11)
s.push(20)
s.push(16)
s.push(10)
s.push(13)
print s.pop()

s.push(15)
s.push(12)
s.sprint()


    
