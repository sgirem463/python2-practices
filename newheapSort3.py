#
# new heap sort
#

import random


def swap(L, i, j):
    tmp = L[i]
    L[i] = L[j]
    L[j] = tmp


def heapSort(L):

    n = len(L)
    print 'length:', n
    print

    for i in range(0, n - 1):
        for j in range(n - 1, i, -1):
            if L[j] < L[j - 1]:
                swap(L, j, j - 1)
            





def heapifyOld(L):
    size = len(L)

    n = (size - 1 - 1) / 2 # n is the index of the last node's parent

    # n's children is 2n+1 and 2n+2

    for i in range(n, -1, -1): # index 0 should be evaluated as well
        if L[i] <= L[2*i + 1]:
            small = i
        else:
            small = 2*i + 1

        if (2*i + 2 <= (size - 1)):
            if L[2*i + 2] <= L[small]:
                small = 2*i + 2

        print 'i, small:', i, small
        if small != i:
            swap(L, i, small)
            L = pushDown(L, i)

    return L


def heapify(L):
    size = len(L)

    n = (size - 1 - 1) / 2 # n is the index of the last node's parent

    # n's children is 2n+1 and 2n+2

    for i in range(n, -1, -1): # index 0 should be evaluated as well
        L = pushDown(L, i)

    return L


def pushDown(L, i):
    n = len(L)

    p = i # initial index of the node to be pushed down

    while True:
        if (2*p + 1) > (n - 1):
            break
        else:
            if L[p] < L[2*p + 1]:
                small = p
            else:
                small = 2*p + 1
        if (2*p + 2) <= (n - 1):
            if L[2*p + 2] < L[small]:
                small = 2*p + 2
        if small != p:
            swap(L, small, p)
            p = small
        else:
            break

    return L
       
                
        

L = []
for i in range(20):
    n = random.randrange(100)
    if n not in L:
        L.append(n)

print L
print 'length:', len(L)

L = heapify(L)

print L

n = len(L)
LL = []
for i in range(n):
    LL.append(L[0])
    L[0] = L[n - i - 1]   # move the last item to the first
    del L[-1]
    L = pushDown(L, i)
    


print LL


    


#
# a heap
#

#
# build a heap from a list
#

#
# 0 based array
# 
#
