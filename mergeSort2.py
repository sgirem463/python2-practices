#mergeSort

import random


def mergeSort(L):
    # split the array in half until the size of the array is 1
    n = len(L)
    if n == 1:
        return

    if (n % 2) == 1:
        middle = n / 2
    else:
        middle = n / 2 - 1

    A = list(L[: middle + 1])
    B = list(L[middle + 1 :])
    mergeSort(A)
    mergeSort(B)

    i = 0
    j = 0
    while True:
        if A[i] < B[j]:
            L[i + j] = A[i]
            i += 1
            if i == len(A):
#                L = L[:i + j] + B[j:]
                for p in range(j, len(B)):
                    L[i + p] = B[p]
                    
                break

        else:
            L[i + j] = B[j]
            j += 1
            if j == len(B):
#                L = L[:i + j] + A[i:]
                for q in range(i, len(A)):
                    L[j + q] = A[q]
                break



def mergeSort2(L):
    # split the array in half until the size of the array is 1
    n = len(L)
    if n == 1:
        return

    if (n % 2) == 1:
        middle = n / 2
    else:
        middle = n / 2 - 1

    A = list(L[: middle + 1])
    B = list(L[middle + 1 :])
    mergeSort2(A)
    mergeSort2(B)

    i = 0
    j = 0
    LL = []
    while True:
        if A[i] < B[j]:
            LL.append(A[i])
            i += 1
            if i == len(A):
                print LL, B[j:]
                LL = LL + B[j:]
#                for p in range(j, len(B)):
#                    L[i + p] = B[p]
                    
                break

        else:
            LL.append(B[j])
            j += 1
            if j == len(B):
                print LL, A[i:]
                LL = LL + A[i:]
#                for q in range(i, len(A)):
#                    L[j + q] = A[q]
                break
    L = []
    for i in range(len(LL)):
        L.append(LL[i])













K = []
for i in range(30):
    n = random.randrange(100)
    if n not in K:
        K.append(n)

print K

mergeSort2(K)


print K
