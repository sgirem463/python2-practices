#
# new selectionSort 
#

import random


def swap(L, i, j):
    tmp = L[i]
    L[i] = L[j]
    L[j] = tmp


def selectionSort(L):

    n = len(L)
    print 'length:', n
    print

    for i in range(0, n):
        for j in range(i, n):
            if L[j] < L[i]:
                swap(L, i, j)


L = []
for i in range(20):
    n = random.randrange(100)
    if n not in L:
        L.append(n)

print L

selectionSort(L)

print L
