# priority queue with heap

import random

def heapify(L, count):
    start = (count - 1 - 1) / 2

    while start >= 0:
        shiftDown(L, start, count)
        start -= 1

def swap(L, p, q):
    tmp = L[p]
    L[p] = L[q]
    L[q] = tmp


def shiftDown(L, start, count): # start is the starting index, count is the current size of unsorted portion

    while start <= ((count - 1 - 1) / 2):
        small = start # starting with swaping with itself, i.e. no change
#        print 'start:', start, 'count:', count, '(count -2) / 2:', (count - 2) / 2
        if L[start] > L[start * 2 + 1]:
            small = start * 2 + 1
        if (start * 2 + 2) < (count - 1):  # may not have right child
            if L[small] > L[start * 2 + 2]:
                small = start * 2 + 2
        if start == small:
            break
        swap(L, start, small)
        start = small

def getMin(A):
    size = len(A)
    r = A[0]
    swap(A, 0, size - 1)
    A.pop()
    shiftDown(A, 0, size - 1)
    return r
    

A = [random.randrange(100) for i in range(30)]
print A

heapify(A, len(A))

print'get mins'

for i in range(20):
    print getMin(A)
    

