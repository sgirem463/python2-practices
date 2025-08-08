
import random

def bubblesort(L):
    n = len(L)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if L[j] < L[j - 1]:
                tmp = L[j]
                L[j] = L[j - 1]
                L[j - 1] = tmp



L = []
for i in range(30):
    n = random.randrange(100)
    if n not in L:
        L.append(n)

print L

bubblesort(L)

print L
    
