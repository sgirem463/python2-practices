
count = 0

def minSquares(m, n):
    global count
    count += 1
    if m == 0 or n == 0:
        minAnswer = 0
    elif (m == n):
        minAnswer = 1
    elif (m > n):
        minAnswer = -1
        for i in range (1, n + 1):
            tmp1 = 1 + minSquares(m - i, n) + minSquares(i, n - i)
            tmp2 = 1 + minSquares(m , n - i) + minSquares(i, m - i)
            tmp = min(tmp1, tmp2)
            if tmp < minAnswer or minAnswer == -1:
                minAnswer = tmp
    elif (m < n):
        minAnswer = -1
        for i in range (1, m + 1):
            tmp1 = 1 + minSquares(m - i, n) + minSquares(i, n - i)
            tmp2 = 1 + minSquares(m , n - i) + minSquares(i, m - i)
            tmp = min(tmp1, tmp2)
            if tmp < minAnswer or minAnswer == -1:
                minAnswer = tmp

#    print 'm = %d, n = %d, minAnswer = %d' % (m, n, minAnswer)
    return minAnswer


#print minSquares(5, 5)
print minSquares(6, 5)
print 'count = ', count
#print minSquares(7, 5)

