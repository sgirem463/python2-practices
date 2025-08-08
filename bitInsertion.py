# number insertion

def insertion(N, M, i, j):
    print 'N:', bin(N)
    print 'M:', bin(M)
    n = 0xffffffff << (j + 1)
    m = 0xffffffff >> (32 - i)
    v = n | m
    print bin(v)
    N = v & N
    print 'new N:', bin(N)
    M = M << i
    print 'new M:', bin(M)
    v = N | M
    print 'v:', bin(v)
    return v


N = 0b10000000000
M = 0b10011
i = 2
j = 6

insertion(N, M, i, j)
