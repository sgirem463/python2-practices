import random



def rotate_matrix(M, n): # Matrix M has size n * n
    LL = []
    for i in range(n):
        L = []
        for j in range(n):
            L.append(M[n-j-1][i])
        LL.append(L)
    return LL
                    


def inplace_rotate_matrix(M, n):
    m = n / 2 # rotate a quarter of the matrix
    for i in range(m):
        # x(i, j) <- x(n - j - 1, i)
        # x(i, j) -> x(j, n - i -1)
        for j in range(m):
            tmp = M[i][j]
            M[i][j] = M[n - j - 1][i]
            M[n - j - 1][i] = M[n - i - 1][n - j - 1]
            M[n - i - 1][n - j - 1] = M[j][n - i - 1]
            M[j][ n - i - 1] = tmp
    return M


LL = []
 
for j in range(10):
	L =[]
	for i in range(10):
		s = ''
		for i in range(4):
			c = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
			s += c
		L.append(s)
	LL.append(L)

print LL
LLL = rotate_matrix(LL, 10)
print
print LLL
LLL = inplace_rotate_matrix(LL, 10)
print
print LLL
