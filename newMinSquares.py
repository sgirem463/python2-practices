#
# minSquares
#

M = []
for i in range(50):
    M.append([])
    for j in range(50):
        M[i].append(float('inf'))

for i in range(50):
    for j in range(50):
        if (i == 0 or j == 0):
            M[i][j] = 0
        elif (i == j):
            M[i][j] = 1


def minSquares(m, n):
    global M
    # print m, n
    if (M[m][n] < float('inf')):
        return M[m][n]
    elif (m == n):
        return 1
    elif (m > n):

        minA = []
        for i in range(1, n + 1):
            minA.append(1 + min(minSquares(m - i, n) + minSquares(i, n - i),
                              minSquares(m, n - i) + minSquares(m - i, i)))

        M[m][n] = min(minA[j] for j in range(n))
        return M[m][n]
            
    else: # m < n
        minA = []
        for i in range(1, m + 1):
            minA.append(1 + min(minSquares(m - i, n) + minSquares(i, n - i),
                              minSquares(m, n - i) + minSquares(m - i, i)))

        M[m][n] = min(minA[j] for j in range(m))
        return M[m][n]







print minSquares(7, 7)
print minSquares(7, 5)
print minSquares(11, 9)
print minSquares(10, 5)


# answer = minSquares(11, 7)
# print answer


