#
# quickSort
#

import random


def swap(L, i, j):
    tmp = L[i]
    L[i] = L[j]
    L[j] = tmp


def quickSort(L):

    n = len(L)
    print 'size:', n

    if n <= 1:
        return L

    # use the first item as the pivot, move the items before and after the pivot
    p = 0 # index is is the beginning of pivot

    for i in range(1, n):
        if L[i] < L[p]:
            tmp = L[p]
            L[p] = L[i]
            L[i] = L[p + 1]
            L[p + 1 ] = tmp
            p += 1

    print 'p:', p
    print L[0 : p]
    print [L[p]]
    print L[p + 1 : n]
    # return (quickSort(L[0 : p]) + [L[p]] + quickSort(L[p + 1 : n]))

    L[0 : p] = quickSort(L[0 : p])
    L[p + 1 : n] = quickSort(L[p + 1 : n])
    return L



L = []
for i in range(20):
    n = random.randrange(100)
    if n not in L:
        L.append(n)

print L
print 'length:', len(L)
print

quickSort(L)

print L
