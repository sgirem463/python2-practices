# radix sort

import random



A = [random.randrange(1000000)  for i in range(200)]
print
print A
print

B = ['{0:06d}'.format(i) for i in A]

print B


print
R = [[] for i in range(10)]
print R

n = 1000000 - 1

digits = 0
while n > 1:
    n /= 10
    digits += 1

print   
print 'digits:',  digits
print

for i in range(digits):
    for n in B:
        d = int(n[digits - i - 1])
        R[d].append(n)
    B = []
    for j in range(10):
        B += R[j]
        R[j] = []


print B

A = []
for i in B:
    A.append(int(i))

print
print A
print

