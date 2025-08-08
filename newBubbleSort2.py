#
# new bubble sort
#

import random


def swap(L, i, j):
    tmp = L[i]
    L[i] = L[j]
    L[j] = tmp


def bubbleSort(L):

    n = len(L)
    print 'length:', n
    print

    for i in range(0, n - 1):
        for j in range(n - 1, i, -1):
            if L[j] < L[j - 1]:
                swap(L, j, j - 1)
            



L = []
for i in range(20):
    n = random.randrange(100)
    if n not in L:
        L.append(n)

print L

bubbleSort(L)

print L
