# bit pairwise swap

def pairwiseSwap(a):
    print a
    print '{0:064b}'.format(a)
    for i in range(32): # assume 64-bits intergers
        left = a & (0b10 << (i * 2))
#        print 'left: {0:064b}'.format(left)

        right = a & (0b1 << (i * 2))
#        print 'right: {0:064b}'.format(right)

        a = a & (~(0b11 << (i * 2)))
#        print 'a: {0:064b}'.format((0b11 << (i * 2)))

#        print 'a: {0:064b}'.format(a)

        a = a | (left >> 1) | (right << 1)

    print '{0:064b}'.format(a)


pairwiseSwap(1234)
pairwiseSwap(9876)


0000000000000000000000000000000000000000000000000000010011010010
0000000000000000000000000000000000000000000000000000100011100001

0000000000000000000000000000000000000000000000000010011010010100
0000000000000000000000000000000000000000000000000001100101101000
