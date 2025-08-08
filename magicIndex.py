# find a magic index, sorted array such that a[i] == i

import random
import sets

def magicIndex(lower, upper):
    if lower == upper:
        if A[lower] == lower:
            print lower, A[lower]
            return
        else:
            return

    middle = (upper + lower) / 2
    print 'middle: %d, A[middle] %d, lower: %d, upper: %d' % (middle, A[middle], lower, upper)
    if A[middle] == middle:
        print middle, A[middle]
    elif A[middle] < middle:
        return magicIndex(middle + 1, upper)
    else:
        if middle > lower:
            return magicIndex(lower, middle - 1)


A = []
for i in range(120):
    A.append(random.randrange(-100, 100))

A = list(sets.Set(A))
A.sort()

size = len(A)
print 'size:', size
print A
print

magicIndex(0, size - 1)

print
print 'checking...'
print
for i in range(size):
    if i == A[i]:
        print i, A[i]
