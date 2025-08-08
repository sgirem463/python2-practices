# intersection of two linked list
# for C, by references, not by values
# make hash table of the first list's item addresses
# Go through the 2nd list to lookup each item's address

# for Python, have to compare values of two list

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
    L1 = [random.randrange(300) for i in range(20)]
    L2 = [random.randrange(300) for i in range(20)]
    print L1
    print L2
    print
    answer = False

    for i in L1:
        hash(i)
    for i in L2:
        if (lookup(i)):
            print i
            answer = True
            break
    
    print answer
    print
    print HashTable
