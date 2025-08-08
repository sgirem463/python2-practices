# quicksort

L = [6, 35, 24, 1, 25, 15, 8, 22, 3, 23, 5, 18, 2, 11, 17, 31, 27, 4, 14, 7, 29, 9, 19, 16, 12]


def quicksort(p, q):
    global L
    oldP = p

    print 'quicksort:', L[p:q+1]
        
    for i in range(p+1, q+1):
        if (L[i] < L[p]): # need to swap and move the pivot point by one position
            if (i == (p + 1)):
                tmp = L[i]
                L[i] = L[p]
                L[p] = tmp
                p = p + 1
            else:
                tmp = L[p]
                L[p] = L[i]
                L[i] = L[p + 1]
                L[p + 1] = tmp
                p = p + 1

    if ((p - oldP) >= 2):
        quicksort(oldP, p-1)
    if ((q - p) >= 2):
        quicksort(p+1, q)


L = [6, 35, 24, 1, 25, 15, 8, 22, 3, 23, 5, 18, 2, 11, 17, 31, 27, 4, 14, 7, 29, 9, 19, 16, 12]
quicksort(0, len(L) - 1)

print L
