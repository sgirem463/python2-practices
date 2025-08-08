# find element in a rotated array

import sets
import random

A = [random.randrange(200)  for i in range(60)]
A = list(sets.Set(A))
A.sort()

print A
sizeA = len(A)
print 'size:', len(A)
print

rotations = random.randrange(sizeA)
print 'rotations:', rotations
B = []
B[:rotations] = A[sizeA - rotations: ]
B[rotations:] = A[: sizeA - rotations]

print B

# find "rotations", binary search the item that the left side is bigger and the righ size is bigger
# i.e. find the smallest item

# first item
# last item
# middle item

middle = sizeA / 2
print 'middle:', '[', middle, ']', B[middle]


def findMin(B, lower, upper, size):
    middle = (upper - lower) / 2 + lower
    print 'lower:', lower, 'upper:', upper, 'middle:', middle, 'value:', B[middle]

    if middle == (size - 1):
        right = 0
    else:
        right = middle + 1
    if middle == 0:
        left = size - 1
    else:
        left = middle - 1

    if B[middle] < B[right] and B[middle] < B[left]:
        return middle
        
    if B[middle] < B[lower]:
        return findMin(B, lower, middle, size)
    else:
        return findMin(B, middle + 1, upper, size)





# minIndex = findMin(B, 0, sizeA - 1, sizeA)

# print 'minIndex:', minIndex, 'value:', B[minIndex]


def findElement(B, size, value):

    if size == 1:
        if B[0] == value:
            print 'found:', value
            return value
        else:
            return -1

    middle = size / 2
    print 'middle', middle, '-', B[middle]
    if B[middle] == value:
        return value

    if (B[middle] > B[0]): # left side is in order
        if (value < B[middle] and value >= B[0]):
            print 'go left'
            return findElement(B[:middle], middle, value)
        else:
            print 'go right'
            return findElement(B[middle + 1:], size - middle - 1, value)
    else: # right side is in order
        if (value > B[middle] and value <= B[size - 1]):
            print 'go right'
            return findElement(B[middle + 1:], size - middle - 1, value)
        else:
            print 'go left'
            return findElement(B[:middle], middle, value)



value = B[random.randrange(len(B))]
print 'value:', value
print

r = findElement(B, len(B), value)

print
print 'answer:', r




    
