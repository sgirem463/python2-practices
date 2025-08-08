# heapsort

import random

'''

0 bzsed array/list
parent index n:
left child index: 2n + 1
right child index: 2n + 2


left or right child index: n
parent index (n - 1) / 2, integer dividing, or floor


'''


def heapify(L, count):
    start = (count - 1 - 1) / 2

    while start >= 0:
        shiftDown(L, start, count)
        start -= 1

def swap(L, p, q):
    tmp = L[p]
    L[p] = L[q]
    L[q] = tmp

    
def heapsort(L, count):
    heapify(L, count)
    swap(L,0, count - 1)
    last = count - 1 - 1 # index of current last unsorted item
    while last >= 0 :
        shiftDown(L, 0, last) # last is the current count
        swap(L, 0, last)
        last -= 1

    print L

def shiftDown(L, start, count): # start is the starting index, count is the current size of unsorted portion

    while start <= ((count - 1 - 1) / 2):
        small = start # starting with swaping with itself, i.e. no change
        print 'start:', start, 'count:', count, '(count -2) / 2:', (count - 2) / 2
        if L[start] > L[start * 2 + 1]:
            small = start * 2 + 1
        if (start * 2 + 2) < (count - 1):
            if L[small] > L[start * 2 + 2]:
                small = start * 2 + 2
        if start == small:
            break
        swap(L, start, small)
        start = small
        


A = [random.randrange(100) for i in range(30)]
print A

heapsort(A, len(A))

