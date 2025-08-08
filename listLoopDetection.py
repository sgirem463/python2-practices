# loop detection
# for C, make a hash table of the address, a loop is detected once a repeated
# address is found

import random

HashTable = {}

def hash(n):
    bucket = n % 10
    if bucket not in HashTable:
        HashTable[bucket] = [n]
    else:
        HashTable[bucket].append(n)


def lookup(n):
    bucket = n % 10
    if bucket not in HashTable:
        return False
    else:
        L = HashTable[bucket]
        if n in L:
            return True
        else:
            return False


if __name__ == '__main__':
    L1 = [random.randrange(300) for i in range(35)]
    print L1
    print
    answer = False

    for i in L1:
        if lookup(i):
            answer = True
            print i
            break
        else:
            hash(i)

    
    print answer
    print
    print HashTable
