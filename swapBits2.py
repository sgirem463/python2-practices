#
# swap odd and even bits of an integer
# e.g. swap bits 0 and 1, swap bits 2 and 3
#

def swapBits(n):

    a = 0x5555555555555555
    b = 0xaaaaaaaaaaaaaaaa
    
    # right shift
    a = a & (n >> 1)

    # left shift
    b = b & (n << 1)

    c = a ^ b

    print '{0:064b}'.format(n)
    print '{0:064b}'.format(c)


swapBits(123456789123456789)
print
swapBits(708935482669934345)
