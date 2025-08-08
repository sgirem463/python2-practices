#
# myQueue class with 2 stacks
#
# queue, first in first out
# with two real stacks
#

class myQueue():
    def __init__(self):
        self.newStack = []
        self.oldStack = []

    def _pop(self):
        try:
            value = self.oldStack.pop()
            return value
        except Exception as ex:
            print Exception
            return None
            

    def _push(self, value):
         self.newStack.append(value)

    def _pushToOldStack(self):
        n = len(self.newStack)
        for i in range(n):
            self.oldStack.append(self.newStack.pop())
        

    def _restoreNewStack(self):
        n = len(self.oldStack)
        for i in range(n):
            self.newStack.append(self.oldStack.pop())

    def enQueue(self, value):
        if len(self.oldStack) > 0:
            self._restoreNewStack()
        self._push(value)

    def deQueue(self):
        if len(self.newStack) > 0:
            self._pushToOldStack()
        return self._pop()

    def pprint(self):
        if len(self.oldStack) > 0:
            print self.oldStack[::-1]
        else:
            print self.newStack
        


q = myQueue()
print q.deQueue()
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)
q.pprint()
q.enQueue(4)
q.enQueue(5)
print q.deQueue()
q.pprint()

q.enQueue(6)
q.pprint()

q.enQueue(7)
q.enQueue(8)
print q.deQueue()
print q.deQueue()
q.pprint()

q.enQueue(9)
q.pprint()

print q.deQueue()
q.pprint()

q.enQueue(10)
q.pprint()

print q.deQueue()
q.pprint()

q.enQueue(11)
q.enQueue(12)
q.enQueue(13)
q.pprint()

