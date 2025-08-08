
'''
Build a hash tabel with each element as "bucket: (index, value)" for all numbers
Go through all numbers,
    for each, lookup its counterpart, keep a set of index pairs (i,j) such
    that (i,j) and (j,i) are considered the same to avoid double counting

'''

import sets
import random


def myhash(i, x):
	bucket = x % 10
	if bucket in htable:
		htable[bucket].append((i, x))
	else:
		htable[bucket] = [(i,x)]

def lookup(x):
	bucket = x % 10
	tableList = htable[bucket]
	answer = []
	for t in tableList:
		if t[1] == x:
			answer.append(t)
	return answer


numbers = [random.randrange(35) for i in range(80)]
numbers.sort()
htable = {}
n = len(numbers)
seen = sets.Set({})
pairs = []

print numbers
print
print 'n:', n
print

for i in range(len(numbers)):
    myhash(i, numbers[i])
    
for i in range(len(numbers)):
	k = lookup(43 - numbers[i])
	for j in k:
		if (i,j[0]) in seen or (j[0],i) in seen:
			continue
		seen.add((i, j[0]))
		pairs.append([numbers[i], j[1]])


print htable
print
print pairs
