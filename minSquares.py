
count = 0


def minSquares(m, n):
    global count
    global M
    
    count += 1
    if m == 0 or n == 0:
        minAnswer = 0
    elif (m == n):
        minAnswer = 1
    elif (m > n):
        minAnswer = -1
        for i in range(1, n + 1):

            if M[m - i][n] == -1:
                a = minSquares(m - i, n)
            else:
                a = M[m - i][n]
                
            if M[i][n - i] == -1:
                b = minSquares(i, n - i)
            else:
                b = M[i][n - i]

            tmp1 = 1 + a + b
            
            if M[m][n - i] == -1:
                a = minSquares(m, n - i)
            else:
                a = M[m][n - i]
            
            if M[i][m - i] == -1:
                b = minSquares(i, m - i)
            else:
                b = M[i][m - i]

            tmp2 = 1 + a + b
            
            tmp = min(tmp1, tmp2)
            if tmp < minAnswer or minAnswer == -1:
                minAnswer = tmp
    elif (m < n):
        minAnswer = -1
        for i in range(1, m + 1):
            if M[m - i][n] == -1:
                a = minSquares(m - i, n)
            else:
                a = M[m - i][n]
                
            if M[i][n - i] == -1:
                b = minSquares(i, n - i)
            else:
                b = M[i][n - i]            
            tmp1 = 1 + a + b

            if M[m][n - i] == -1:
                a = minSquares(m, n - i)
            else:
                a = M[m][n - i]
                
            if M[i][m - i] == -1:
                b = minSquares(i, m - i)
            else:
                b = M[i][m - i]
            tmp2 = 1 + a + b

            tmp = min(tmp1, tmp2)
            if tmp < minAnswer or minAnswer == -1:
                minAnswer = tmp


    M[m][n] = minAnswer
    return minAnswer

M = []
def initM():
    global M
    X = []
    for i in range(100):
        X.append(-1)

    M = []
    for i in range(100):
        M.append(list(X))



count = 0
initM()
print '(6, 5)', minSquares(6, 5),  ', count =', count
count = 0
initM()
print '(13, 11)', minSquares(13, 11), ', count =', count
count = 0
initM()
print '(13, 12)', minSquares(13, 12), ', count =', count
count = 0
initM()
print '(12, 11)', minSquares(12, 11), ', count =', count
count = 0
initM()
print '(12, 10)', minSquares(12, 10), ', count =', count
count = 0
initM()
print '(11, 10)', minSquares(11, 10), ', count =', count
count = 0
initM()
print '(19, 17)', minSquares(19, 17), ', count =', count
count = 0
initM()
print '(19, 13)', minSquares(19, 13), ', count =', count

#print minSquares(7, 5)

print
for i in range(10):
    for j in range(10):
        print M[i][j],
    print
print
