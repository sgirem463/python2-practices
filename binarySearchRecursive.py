#
# recursive binary search
#
#
# find value a in list L
#
def bSearch(a, L):
    size == len(L)
    if size == 0:
        return False
    elif size == 1:
        if a == L[0]:
            return True
        else:
            return False

    mid = size // 2

    if a == L[mid]:
        return True
    elif a < L[mid]:
        bSearch(a, L[:mid]
    else:
        if (mid + 1) >= size:
            return False
        bSearch(a, L[mid + 1:])
