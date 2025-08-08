# drawline

def drawline(width, length, x1, x2, y):

    print 'x2 - x1:', (x2 - x1)
    # pixel start with (0, 0)
    p1 = y * width + x1  # index of the bigenning bit
    p2 = y * width + x2  # index of the ending bit

    byteCount1 = p1 / 8  # number of bytes to be set to 0
    bitCount1 = p1 % 8   # number of additional bits to be set to 0
    array = []

    for i in range(byteCount1):
        array.append(0)

    byteCount3 = 0

    if (bitCount1 != 0):
        byteCount3 += 1
        byte1 = 0xff  # all ones
        byte1 = (byte1 << bitCount1) & 0xff # shift 0's in
        array.append(byte1)


    byteCount2 = (x2 - x1) / 8  # number of bytes to be set to 1
    bitCount2 = (x2 - x1 - bitCount1) % 8  # number of additional bits to be set to 1

    for i in range(byteCount1 + 1, byteCount1 + byteCount2 + 1):
        array.append(0xff)


    if (bitCount2 != 0):
        byteCount3 += 1
        byte2 = 0
        for i in range(bitCount2):  # or byte = 2 ** bitcount2 - 1
            byte2 |= 1 << i
        array.append(byte2)


    for i in range(byteCount1 + byteCount2 + byteCount3 + 1, (width * length) / 8 + 1):
        array.append(0)
        
    return array

    





a = drawline(256, 192, 27, 215, 77)
print 'size a:', len(a)
print
print a
n = a.index(0xff)
print '{0:08b}'.format(a[n-1])
print n
m = a.index(0, n)
print m
print '{0:08b}'.format(a[m - 1])


