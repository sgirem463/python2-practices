#
# new mergeSort
#


import random


def swap(L, i, j):
    tmp = L[i]
    L[i] = L[j]
    L[j] = tmp


def mergeSort(L):

    n = len(L)
    print 'length:', n
    if n <= 1:
        return L
        



    h = n // 2  # half point    
    # divide to two halves for recursive mergesort
    L1 = mergeSort(L[0 : h])
    L2 = mergeSort(L[h : n])
    l1 = len(L1)
    l2 = len(L2)

    # merge the two halves
    L = []
    p1 = 0
    p2 = 0
    for i in range(n):
        if (L1[p1] <= L2[p2]):
            L.append(L1[p1])
            p1 += 1
            if p1 >= l1:
                L = L + L2[p2:]
                break
        else:
            L.append(L2[p2])
            p2 += 1
            if p2 >= l2:
                L = L + L1[p1:]
                break            
            
    return L
            



L = []
for i in range(20):
    n = random.randrange(100)
    if n not in L:
        L.append(n)

print L

L = mergeSort(L)

print L
