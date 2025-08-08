#
# hash table implementation for numbers
#
# a list of 10 lists
# each internal list represents a bucket
# a simple hash of mod / 10
#

import random

HTable = []

def myHash(n):
    return n % 10

def insertHTable(n):
    global Htable
    h = myHash(n)
    HTable[h].append(n)

def printHTable():
    global HTable
    for i in range(10):
        print HTable[i]

def lookup(n):
    print 'lookup', n,
    h = myHash(n)
    for i in range(len(HTable[h])):
        if HTable[h][i] == n:
            print ', found', h, i, '!!!'
            return
    print ', not found'


    
for i in range(10):
    HTable.append([])

N = []
for i in range(100):
    N.append(random.randrange(500))

print N

print

for i in N:
    insertHTable(i)


printHTable()

print

for j in range(30):
    lookup(random.randrange(500))



