
count = 0


def minSquares(m, n):
    global count
    global M
    
    count += 1
    if m == 0 or n == 0:
        minAnswer = 0
        T[m][n] = [(m, n)]
    elif (m == n):
        minAnswer = 1
        T[m][n] = [(m, n)]
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

            if tmp == minAnswer:
                if tmp1 < tmp2:
                    T[m][n].append((m, n, (i, i), (m - i, n), (i, n - i)))
                elif tmp1 > tmp2:
                    T[m][n].append((m, n, (i, i), (m, n - i), (i, m - i)))
                else:
                    T[m][n].append((m, n, (i, i), (m, n - i), (i, m - i)))
                    T[m][n].append((m, n, (i, i), (m - i, n), (i, n - i)))
                    
            if tmp < minAnswer or minAnswer == -1:
                minAnswer = tmp
                T[m][n] = []
                if tmp1 < tmp2:
                    T[m][n].append((m, n, (i, i), (m - i, n), (i, n - i)))
                elif tmp1 > tmp2:
                    T[m][n].append((m, n, (i, i), (m, n - i), (i, m - i)))
                else:
                    T[m][n].append((m, n, (i, i), (m, n - i), (i, m - i)))
                    T[m][n].append((m, n, (i, i), (m - i, n), (i, n - i)))

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


 ## equal case append, less than case reset
            tmp = min(tmp1, tmp2)

            if tmp == minAnswer:
                if tmp1 < tmp2:
                    T[m][n].append((m, n, (i, i), (m - i, n), (i, n - i)))
                elif tmp1 > tmp2:
                    T[m][n].append((m, n, (i, i), (m, n - i), (i, m - i)))
                else:
                    T[m][n].append((m, n, (i, i), (m, n - i), (i, m - i)))
                    T[m][n].append((m, n, (i, i), (m - i, n), (i, n - i)))

            if tmp < minAnswer or minAnswer == -1:
                minAnswer = tmp
                T[m][n] = []
                if tmp1 < tmp2:
                    T[m][n].append((m, n, (i, i), (m - i, n), (i, n - i)))
                elif tmp1 > tmp2:
                    T[m][n].append((m, n, (i, i), (m, n - i), (i, m - i)))
                else:
                    T[m][n].append((m, n, (i, i), (m, n - i), (i, m - i)))
                    T[m][n].append((m, n, (i, i), (m - i, n), (i, n - i)))               


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


T = []
def initT():
    global T
    X = []
    for i in range(100):
        X.append([])

    T = []
    for i in range(100):
        T.append(list(X))


def traceT(m, n):
    print T[m][n]
    for i in range(len(T[m][n])):
        if not isinstance(T[m][n][i], int) and len(T[m][n][i]) > 2:
            traceT(T[m][n][i][3][0], T[m][n][i][3][1])
            traceT(T[m][n][i][4][0], T[m][n][i][4][1])


initT()
count = 0
initM()
print '(6, 5),', minSquares(6, 5),  ', count =', count
traceT(6, 5)
# count = 0
# initM()
# print
# print '(13, 11),', minSquares(13, 11), ', count =', count
# traceT(13, 11)

# count = 0
# initM()
# print
# print '(13, 12),', minSquares(13, 12), ', count =', count
# traceT(13, 12)

# count = 0
# initM()
# print
# print '(12, 11),', minSquares(12, 11), ', count =', count
# traceT(12, 11)

count = 0
initM()
print
print '(12, 10),', minSquares(12, 10), ', count =', count
traceT(12, 10)

count = 0
initM()
print
print '(11, 10),', minSquares(11, 10), ', count =', count
traceT(11, 10)


#print minSquares(7, 5)

print
for i in range(10):
    for j in range(10):
        print M[i][j],
    print
print
