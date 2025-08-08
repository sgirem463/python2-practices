# robot move, r rows and c columns with some off limit cells
# move from top left to lower right, by down or right

import random

M = []
for i in range(10):
    A = []
    for j in range(10):
        if random.randrange(100) < 15:
            A.append(1)
        else:
            A.append(0)
    M.append(list(A))

for i in range(10):
    for j in range(10):
        print M[i][j],
    print


def findPath(a, b, r, c, L):
    global reached
    print '( %d, %d)' % (a, b)
    L.append((a, b))
    if a == r and b == c:
        print 'reached bottom right'
        print L
        reached = True
    if reached:
        return
    if a < r and not M[a + 1][b]:
        findPath(a + 1, b, r, c, L)
    if reached:
        return
    if b < c and not M[a][b + 1]:
        findPath(a, b + 1, r, c, L)
    if reached:
        return
    if a < r and b < c:
        if M[a + 1][b] and M[a][b + 1]:
            M[a][b] = 1
    if a < r and b == c:
        if M[a + 1][b]:
            M[a][b] = 1
    if a == r and b < c:
        if M[a][b + 1]:
            M[a][b] = 1
    
reached = False

if not M[0][0]:
    findPath(0, 0, 9, 9, [])

for i in range(10):
    for j in range(10):
        print M[i][j],
    print
