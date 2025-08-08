'''
Given a number Lookup the hash table to see if the the counter part number(s)
exit, build the answer if any, insert the number to hash table

'''



import random

def lookup(x):
	bucket = x % 10
	if bucket in htable:
		tableList = htable[bucket]
	else:
		return []
	answer = []
	for y in tableList:
		if y == x:
			answer.append(y)
	return answer

def myhash( x):
	bucket = x % 10
	if bucket in htable:
		htable[bucket].append( x)
	else:
		htable[bucket] = [x]


numbers = [random.randrange(35) for i in range(80)]
numbers.sort()
answer =[]
htable = {}
n = len(numbers)

print numbers
print
print 'n:', n
print

for i in range(n):
	L = lookup(43 - numbers[i])
	for j in L:
		answer.append([numbers[i],j])
	myhash(numbers[i])


print htable
print
print answer
