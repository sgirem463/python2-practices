#
# duplicated numbers in an array
#

hashT = {}

for i in range(100):
    hashT[i] = []


def insertH(n):
    global hashT

    bucket = n % 100
    if n in hashT[bucket]:
        hashT[bucket].append(n)
        return True
    else:
        hashT[bucket].append(n)
        return False       



    
def findDuplicates(L):
    dups = []
    
    for i in L:
        if insertH(i):
            dups.append(i)

    return dups


L = [45, 34, 66, 21, 28, 3, 11, 7, 89, 73, 44, 27, 15, 98, 66, 70, 22, 21, 7]

print findDuplicates(L)

for i in range(100):
    print i, hashT[i]
