# mergesort

def mergesort(L):
    # divide in half and call recursively
    n = len(L)
    h = int(n/2)
    print 'mergesort-a', L

    # pass by object reference doesn't seem to work here, create new lists for now
    if (h >= 2):
        mergesort(L[0 : h])

        print 'mergesort-1', L[0 : h]
    if ((n - h) >= 2):
        mergesort(L[h : n])

        print 'mergesort-2', L[h : n]


    # merge the two halves
    p = 0
    q = h
    newL = []
    for i in range(n):
        if (L[p] < L[q]):
            newL.append(L[p])
            if (p == (h - 1)):
                newL = newL + L[q : n]
                break
            else:
                p = p + 1
        elif (L[p] > L[q]):
            newL.append(L[q])
            if (q == (n - 1)):
                newL = newL + L[p : h]
                break
            else:
                q = q + 1

    for i in range(len(newL)):
        L[i] = newL[i]
    print 'mergesort-b', L

L1 = [6, 35, 24, 1, 25, 15, 8, 22, 3, 23, 5, 18, 2, 11, 17, 31, 27, 4, 14, 7, 29, 9, 19, 16, 12]

mergesort(L1)
print L1
