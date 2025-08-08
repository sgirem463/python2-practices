import random

def insertionSort(L):
    n = len(L)
    for i in range(1, n):
        for j in range(i , 0, -1):
            if L[j] < L[j - 1]:
                tmp = L[j]
                L[j] = L[j - 1]
                L[j - 1] = tmp
            else:
                break
            


    

L = []
for i in range(30):
    n = random.randrange(100)
    if n not in L:
        L.append(n)

print L

insertionSort(L)

print L

L = []
for i in range(30):
    n = random.randrange(100)
    if n not in L:
        L.append(n)

print
print L
insertionSort(L)
print L
