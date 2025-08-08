import random

def zero_matrix(M, n): # matrix M of size n * n
    columns = []
    rows = []
    for i in range(n):
        for j in range(n):
            if (M[i][j] == 0):
                if i not in rows:
                    rows.append(i)      
                if j not in columns: 
                    columns.append(j)   
    for i in rows:
        for j in range(n):
            M[i][j] = 0 
    for j in columns:
        for i in range(n):
            M[i][j] = 0 
    for i in range(n):
        for j in range(n):
            print "%3d" % M[i][j],
        print
    return M


n = 10
zc = 0 # zero count
LL = []

for i in range(n):
    L = []
    for j in range(n):
        number = random.randrange(n * 2)
        if number == 0:
            zc += 1     
        L.append(number)
    LL.append(L)
    for j in range(n):
        print "%3d" % L[j],
    print

print 'zero count:', zc
print
zero_matrix(LL, n)

