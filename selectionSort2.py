import random

def bubblesort(L):
    n = len(L)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if L[j] < L[j - 1]:
                tmp = L[j]
                L[j] = L[j - 1]
                L[j - 1] = tmp





def selectionSort(L):
    n = len(L)
    for i in range(n):
        for j in range(i + 1, n):
            if L[j] < L[i]:
                tmp = L[j]
                L[j] = L[i]
                L[i] = tmp


def selectionSort2(L):
    n = len(L)
    for i in range(n):
        mIndex = i
        for j in range(i + 1, n):
            if L[j] < L[mIndex]:
                mIndex = j
        tmp = L[i]
        L[i] = L[mIndex]
        L[mIndex] = tmp



    

L = []
for i in range(30):
    n = random.randrange(100)
    if n not in L:
        L.append(n)

print L

selectionSort(L)

print L

L = []
for i in range(30):
    n = random.randrange(100)
    if n not in L:
        L.append(n)

print
print L
selectionSort2(L)
print L


