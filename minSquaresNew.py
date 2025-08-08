
#
# minSquares() new implementations
#
#
# define minSquares(m, n) to return the minimal number of squares to cover m x n cells
# how to make sure it does the given job
#



def minSquares(m, n):

    minA = float('inf')

    if m == 0 or n == 0:
        return 0
    if m == n:
        return 1
    
    elif m < n:
        for i in range(1, m + 1):
            a = 1 + minSquares(i, m - i) + minSquares(m, n - i)
            if a < minA:
                minA = a

    else:
        for i in range(1, n + 1):
            a = 1 + minSquares(i, n - i) + minSquares(n, m - i)
            if a < minA:
                minA = a

    return minA



#
# create a 2 dimentional array/matrix
#
INVALID = -1
a = []
for i in range(20):
    a.append(INVALID)
MIN = []
for i in range(20):
    MIN.append(list(a))
    



def minSquares2(m, n):
    global MIN

    minA = float('inf')

    if m == 0 or n == 0:
        minA = 0
    if m == n:
        minA = 1
    
    elif m < n:
        for i in range(1, m + 1):
            if MIN[i][m - i] != INVALID:
                p = MIN[i][m - i]
            else:
                p = minSquares2(i, m - i)

            if MIN[m][n - i] != INVALID:
                q = MIN[m][n - i]
            else:
                q = minSquares2(m, n - i)






            a = 1 + p + q
            if a < minA:
                minA = a

    else:
        for i in range(1, n + 1):
            if MIN[i][n - i] != INVALID:
                p = MIN[i][n - i]
            else:
                p = minSquares2(i, n - i)

            if MIN[n][m - i] != INVALID:
                q = MIN[n][m - i]
            else:
                q = minSquares2(n, m - i)

            a = 1 + p + q
            if a < minA:
                minA = a

    MIN[m][n] = minA
    return minA



INVALID = -1
a = []
for i in range(20):
    a.append(INVALID)
T = []
for i in range(20):
    T.append(list(a))

    

def minSquares3(m, n):
    global MIN
    global T

    minA = float('inf')

    if m == 0 or n == 0:
        minA = 0
        trace = 0
    if m == n:
        minA = 1
        trace = n
    elif m < n:
        for i in range(1, m + 1):
            if MIN[i][m - i] != INVALID:
                p = MIN[i][m - i]
            else:
                p = minSquares3(i, m - i)

            if MIN[m][n - i] != INVALID:
                q = MIN[m][n - i]
            else:
                q = minSquares3(m, n - i)
            a = 1 + p + q


            if MIN[i][n - i] != INVALID:
                p = MIN[i][n - i]
            else:
                p = minSquares3(i, n - i)

            if MIN[m - i][n] != INVALID:
                q = MIN[m - i][n]
            else:
                q = minSquares3(m - i, n)


            b = 1 + p + q
            a = min(a, b)
            if a < minA:
                minA = a
                trace = i

    else:
        for i in range(1, n + 1):
            if MIN[i][n - i] != INVALID:
                p = MIN[i][n - i]
            else:
                p = minSquares3(i, n - i)

            if MIN[n][m - i] != INVALID:
                q = MIN[n][m - i]
            else:
                q = minSquares3(n, m - i)
            a = 1 + p + q


            if MIN[i][m - i] != INVALID:
                p = MIN[i][m - i]
            else:
                p = minSquares3(i, m - i)

            if MIN[m][n - i] != INVALID:
                q = MIN[m][n - i]
            else:
                q = minSquares3(m, n - i)
            b = 1 + p + q


            a = min(a, b)
            if a < minA:
                minA = a
                trace = i

    MIN[m][n] = minA
    T[m][n] = trace
    return minA











a = 5
b = 6
print a, b
print minSquares(a, b)
print


a = 8
b = 5
print a, b
print minSquares(a, b)
print


a = 11
b = 9
print a, b
print minSquares(a, b)
print
            


a = 5
b = 6
print a, b
print minSquares2(a, b)
print


a = 8
b = 5
print a, b
print minSquares2(a, b)
print


a = 11
b = 9
print a, b
print minSquares2(a, b)
print


a = 13
b = 11
print a, b
print minSquares2(a, b)
print


a = 13
b = 12
print a, b
print minSquares2(a, b)
print



a = 19
b = 17
print a, b
print minSquares3(a, b)
print


INVALID = -1
a = []
for i in range(20):
    a.append(INVALID)
MIN = []
for i in range(20):
    MIN.append(list(a))


a = 19
b = 13
print a, b
print minSquares3(a, b)
print


for i in range(20):
    print MIN[i]
print
for i in range(20):
    print T[i]
print

# for i in range(20):
#    for j in range(20):
#        print i, j,'=', T[i][j],
#    print
        
