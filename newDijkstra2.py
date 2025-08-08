#
# dijkstra, shortest path
#

import sys

N = 10

D = []

for i in range (N):
    D.append([])
    for j in range(N):
        if (i == j):
            D[i].append(0)
        else:
            D[i].append(float('inf'))


for i in range(N):
    print D[i]

                   
D[1][2] = 10
D[1][5] = 100
D[1][4] = 30
D[2][3] = 50
D[3][5] = 10
D[4][3] = 20
D[4][5] = 60


S = {1}

T = {2,3,4,5}

print len(T)


while True:
    print S, T
    if len(T) == 0:
        break
    dm = float('inf')
    for v in S:
        for w in T:
            dw = D[1][v] + D[v][w]
            if dw < dm:
                dm = dw
                p = v
                q = w
    S.add(q)
    T.remove(q)
    if (D[1][p] + D[p][q] < D[1][q]):
        D[1][q] = D[1][p] + D[p][q]

for i in range(N):
    print D[i]

