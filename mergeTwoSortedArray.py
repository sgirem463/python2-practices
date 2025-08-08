# merge two sorted arrays

import random

sizeA = 30
sizeB = 20

A = [random.randrange(100)  for i in range(sizeA)]
B = [random.randrange(100)  for i in range(sizeB)]
A.sort()
B.sort()

for i in range(35):
    A.append('X')

print A
print B


n = len(A)

p = sizeA - 1 # index of the last item with value in A
q = sizeB - 1 # index of the last item in B

r = n - 1 # index of the last item in the complete array A


while True:
    if A[p] > B[q]:
        A[r] = A[p]
        A[p] = 'X'
        p -= 1
        r -= 1
        if p < 0:
            A[r - q:r + 1] = B[: q + 1]
            for i in range(q + 1):
                A[i] = 'X'
            break
    elif A[p] == A[q]:
        A[r] = A[p]
        A[p] = 'X'
        A[r - 1] = B[q]
        p -= 1
        q -= 1
        if p < 0 and q < 0:
            break
        if p < 0:
            A[r - q:r + 1] = B[: q + 1]
            for i in range(q + 1):
                A[i] = 'X'
            break
        if q < 0:
            A[r - p:r + 1] = A[: p + 1]
            for i in range(p + 1):
                A[i] = 'X'
            break
        r -= 2
    else:
        A[r] = B[q]
        q -= 1
        r -= 1        
        if q < 0:
            A[r - p:r + 1] = A[: p + 1]
            for i in range(p + 1):
                A[i] = 'X'
            break

print

print A

print 'size:', len(A) - A.count('X')
