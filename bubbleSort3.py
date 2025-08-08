#
# bubble sort
#


def bubble(L):
    #
    # comparison from last to current smallest
    # from last (always item n - 1) to ith smallest
    #
    n = len(L)
    for i in range(0, n-1):
        for j in range(n-1, i, -1):
            if L[j] < L [j-1]:
                tmp = L[j-1]
                L[j-1] = L[j]
                L[j] = tmp

    return L


def swap(L, i, j):
    tmp = L[i]
    L[i] = L[j]
    L[j] = tmp
    

def selectionSort(L):
    n = len(L)
    #
    # repeat for n - 1 positions, start with position 0 which should
    # hold the smallest item, postion 1 (2nd postion) should hold the
    # 2nd smallest item
    # go down the list and compare each item with the one in the current
    # smallest position, swap if the the item is smaller
    #
    for i in range(n - 1):
        for j in range(i + 1, n):
            if L[j] < L[i]:
                swap(L, i, j)



def quickSort(L):
    print L
    n = len(L)
    if n <= 1:
        return L
    p = 0 # the pivot item

    #
    # move the smaller numbers to the left of the pivot
    # pivot will change its position over time
    #
    for i in range(1, n):
        if L[i] < L[p]:
#            tmp = L[p + 1]
#            L[p + 1] = L[p]        
#            L[p] = L[i]
#            L[i] = tmp
#            tmp = L[p]
#            tmp2 = L[p + 1]
#            L[p] = L[i]
#            L[p + 1] = tmp
#            L[i] = tmp2
            tmp = L[p]
            L[p] = L[i]
            L[i] = L[p + 1]
            L[p + 1] = tmp
            p += 1
            
    print 'p = ', p, 'L[p] = ', L[p]
    L1 = quickSort(L[:p])
    if p < (n - 1):
        L2 = quickSort(L[p + 1:])
    else:
        L2 = []
    L = L1 + [L[p]] + L2
    print 'L = ', L
    return L



    

LL = [7, 3, 6, 9, 2, 1, 5, 13, 8, 4, 0, 10]
print LL


K = bubble(LL)

print 'bubbleSort'
print K

import random
LL = []
for i in range(50):
    n = random.randrange(100)
    if n not in LL:
        LL.append(n)
print
print LL
K = bubble(LL)
print
print LL


print
print '----------------------------------------------------'
print 'selectionSort'
print
LL = []
for i in range(50):
    n = random.randrange(100)
    if n not in LL:
        LL.append(n)

print LL
print
selectionSort(LL)

print LL

print
print '----------------------------------------------------'
print 'quickSort'
print
LL = []
for i in range(10):
    n = random.randrange(100)
    if n not in LL:
        LL.append(n)

print LL
print
LL = quickSort(LL)

print LL


