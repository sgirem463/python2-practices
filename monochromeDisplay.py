
#
# drawline
#

#
# bitmap, black and white, 1 as black
# assuming the left upper corner is (0, 0)
#
# represented by a list of bytes 0xXY
#
# horizonal line
#
def drawLine(screen, width, x1, x2, y):


#
# wuth Python, the easiest way is to put all these bits into a list, then transform the list into
# a sequence of bytes.
#

    #
    # firsr y lines will be all 0s
    # the yth line has leading 0s until position x1,
    #
    # calculate how many leading bits will be 0s, follow by (x2 - x1) bits of 1s,
    # then all 0s
    #

    nZeros1 = width * y + x1
    nOnes1 = x2 - x1

    #
    # little endian
    #

    #
    # fill leading zero bytes
    #
    nZeroBytes = nZeros1 / 8
    for i in range (nZeroBytes):
        screen[i] = 0

    # fill the partial 0/1 byte with 1s
    byte = 0xff << (nZeros1 % 8)

    #
    # how many 1 bits in the partial byte?
    #

    byte = 0
    if nOnes1 > (8 - (nZeros1 % 8)):
        byte = 0xff << (nZeros1 % 8)
    else:
        for i in range(nOnes1):
            byte |= 1 << i
        byte = 0xff << (nZeros1 % 8)
    screen[nZeroBytes] = byte

    nOnes1 -= (8 - (nZeros1 % 8))

    nOnes1Bytes = nOnes1 / 8

    for i in range(nOnes1Bytes):
        screen[nZeroBytes + i] = 0xff
        
    nOnes1RemainingBits = nOnes1 % 8
    byte = 0
    for i in range(nOnes1RemainingBits):
        byte |= 1 << i
        





    p = 0
    for i in (nZeros1 % 8):
        p |= 1 << i


    
    screen[nZeroBytes]

    nOnes2 = nOnes1 - (nZeros1 / 8)

    #
    # fill the bytes of all 1s, i.e. 0xff
    for i in range(nOnes2 / 8):
        pass

    #
    # fill the remianing 1s
    #
    for j in (nOnes2 % 8):
        pass






    nOnes1Bytes = nOnes1 / 8
    
        
    
