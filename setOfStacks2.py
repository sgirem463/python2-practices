#
#

class StackEmpty(Exception):
    pass

#
# Set of stacks
#

class SetOfStacks():

    threshold = 5
    
    def __init__(self):
        self.size = 0
        self.totalSize = 0
        self.stackIndex = 0
        self.SetOfStacks = []
        self.SetOfStacks.append([])
        

    def push(self, value):

        self.SetOfStacks[self.stackIndex].append(value)
        self.size += 1
        self.totalSize += 1
        if self.size == SetOfStacks.threshold:
            self.stackIndex += 1
            self.SetOfStacks.append([])
            self.size = 0
        

    def pop(self):
        try:
            if self.totalSize == 0:
                raise StackEmpty()
        
            if self.size == 0:
                self.SetOfStacks.pop()
                self.stackIndex -= 1
                self.size = SetOfStacks.threshold
                
            value = self.SetOfStacks[self.stackIndex].pop()
            self.totalSize -= 1
            self.size -= 1
            return value
        
        except Exception as ex:
            print ex
            print type(ex)

    def printStack(self):
        print self.SetOfStacks
        


myStack = SetOfStacks()
print myStack.pop()
myStack.push(1)
myStack.push(2)
myStack.push(3)
print myStack.pop()
myStack.push(4)
myStack.push(5)
myStack.push(6)
myStack.push(7)
myStack.push(8)
print myStack.pop()
myStack.printStack()
myStack.push(9)
myStack.push(10)
myStack.push(11)
myStack.push(12)
myStack.push(13)
myStack.push(14)
myStack.push(15)
myStack.push(16)
myStack.push(17)
myStack.push(18)
myStack.printStack()

print myStack.pop()
print myStack.pop()
print myStack.pop()
print myStack.pop()
print myStack.pop()
print myStack.pop()
myStack.printStack()

print myStack.pop()
print myStack.pop()
myStack.printStack()

print myStack.pop()
print myStack.pop()
print myStack.pop()
myStack.printStack()

print myStack.pop()
print myStack.pop()
print myStack.pop()
print myStack.pop()
print myStack.pop()
print myStack.pop()
print myStack.pop()
print myStack.pop()
print myStack.pop()
print myStack.pop()
print myStack.pop()

        


    
