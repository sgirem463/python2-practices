#
#

import math

def bitInsert(m, n, i, j):
    print 'm', bin(m)
    print 'n', bin(n)
    print 'i, j', i, j

    nBits = int(math.floor(math.log(m, 2) + 1))
    print 'nBits', nBits

    p = 0
    for x in range(nBits):
        p = p | 1 << x

    n1 = n & (~p)
    n2 = n1 ^ (m << i)

    print bin(n2)



bitInsert(0b10011, 0b1000000000000, 2, 6)
    
        

    

    
