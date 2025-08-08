#
# myQueue class with 2 stacks
#
# queue, first in first out, kind of needs two pointers or access to
# both ends
# internally, should use push and pop on those two stacks
# probably push to one stack and pop from the other
#

class myQueue():
    def __init__(self):
        LQueue = []
        headStackIndex = 0
        tailStackIndex = 0
        
        
    def _push(self, value):
        LQueue.insert(0, value)
        tailStackIndex += 1


    def _pop(self):
        value = LQueue.pop()
        

        
    def enQueue(self, value):
        # push to the headStack
        _push(value)
        
        pass

    def deQueue(self):
        
        pass
        return value

    
