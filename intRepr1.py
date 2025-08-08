#
# bit representations
#

def intRepr(n):
    L = []
    while n != 0:
        if n & 1:
            L.append(1)
        else:
            L.append(0)
        n = n >> 1


    L.reverse()
    for i in range(len(L)):
        print "{0:1d}".format(L[i]),

    print


def realRepr(n):
    L = []
    if n >= 1:
        print 'error'
        return

    count = 1

    b = n
    L = []
    while b != 0 and count <= 32:
        a = b * 2
        
        if a >= 1:
            L.append(1)
            b = a - 1
        else:
            L.append(0)
            b = a

        count += 1


    print '0.',
    for i in range(len(L)):
        print '{0:1d}'.format(L[i]),
    print


    

intRepr(61)
intRepr(100)
intRepr(88)
intRepr(255)
intRepr(1024)


realRepr(0.625)

realRepr(0.72)
realRepr(0.6875)
