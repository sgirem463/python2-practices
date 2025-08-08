
# indexList will keep index of the stack list such that
# stack[indexList[i]] > stack[indexList[i + 1]]

# stack = [3, 5, 1, 2]
# indexList = [1, 0, 3, 2]

class newStack:
    def __init__(self):
        self.stack = []
        self.indexList = []
        self.size = 0

    def push(self, n):
        self.stack.append(n)
        print 'stack', self.stack
        self.size += 1
        index = self.size - 1
        inserted = False
        if self.size == 1:
            self.indexList.append(0)
        else:
            for i in range(self.size - 1): # indexList is 1 less at this point
                if n < self.stack[self.indexList[i]]:
                    self.indexList.insert(i, index)
                    inserted = True
                    break
            if (not inserted):
                self.indexList.append(index)
        print 'indexList', self.indexList

    def pop(self):
        r = self.stack.pop()
        self.size -= 1
        index = self.size # index to be removed from indexList
        self.indexList.remove(index) # there is the built in function
        print 'indexList', self.indexList
        return r

    def myMin(self):
        index = self.indexList[0]
        self.indexList = self.indexList[1:]

        r = self.stack[index]
        self.size -= 1
        self.stack = self.stack[:index] + self.stack[index + 1:]
        for i in range(self.size):
            if self.indexList[i] > index:
                self.indexList[i] -= 1
        print 'indexList', self.indexList

        return r



s = newStack()
s.push(3)
s.push(5)
s.push(1)
s.push(2)
s.push(8)
s.push(4)
s.push(6)

print s.stack
print s.indexList

print s.pop()
print s.pop()
print s.myMin()
print s.myMin()

print s.stack
print s.indexList


'''
        
        [3]
        [0]
        [3,5]
        [0,1]
        [3,5,1]
        [2,0,1]
        [3,5,1,2]
        [2,3,0,1]
'''
