# quicksort


def quicksort(p, q):
    global L
    oldP = p

    print 'quicksort:', L[p:q+1]
        
    for i in range(p+1, q+1):
        if (L[i] < L[p]): # need to swap and move the pivot point by one position
             tmp = L[p]
             L[p] = L[i]
             L[i] = L[p + 1]
             L[p + 1] = tmp
             p = p + 1

    if ((p - oldP) >= 2):
        quicksort(oldP, p-1)
    if ((q - p) >= 2):
        quicksort(p+1, q)





def quickSort(L, a, b):
    if (a == b):
        return
    
    p = a # pivot

    for i in range(a + 1, b + 1):
        if L[i] < L[p]:
            # move L[p+1] to L[i], move L[i] to L[p], move L[p] to L[p+1]
            tmp = L[i]
            L[i] = L[p + 1]
            L[p + 1] = L[p]
            L[p] = tmp
            p = p + 1

    print [a, p - 1], [p + 1, b]
    
    if (a < (p - 1)):
        quickSort(L, a, p - 1)
    if ((p + 1) < b):
        quickSort(L, p + 1, b)
    
    








L = [6, 35, 24, 1, 25, 15, 8, 22, 3, 23, 5, 18, 2, 11, 17, 31, 27, 4, 14, 7, 29, 9, 19, 16, 12]
print L
# L = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
quicksort(0, len(L) - 1)

print L

L = [6, 35, 24, 1, 25, 15, 8, 22, 3, 23, 5, 18, 2, 11, 17, 31, 27, 4, 14, 7, 29, 9, 19, 16, 12]
quickSort(L, 0, len(L) - 1)
print L
