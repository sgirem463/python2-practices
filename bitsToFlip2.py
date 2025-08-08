
#
# n & (n - 1) == 0
#

# n - 1 == (~n)
#
# n == 2 ** K
#

#
# number of bits to flip to convert integer A to integer B
#

def bitsToFlip(m, n):
    a = m ^ n

    bits = 0

    while a != 0:
        bits += (a & 1)
        a = a >> 1
    
#    for i in range(64):
#        if (1 << i) & a != 0:
#            bits += 1

    return bits

print bitsToFlip(29, 15)

        

#
# c = c & (c - 1), will cler the least significant bit of c
#
# c - 1,
#    if the real LSB is 1 it will be cleared
#    if the real LSB is not 1 and the lowest 1 is at position n
#         the operation becomes
#         (2 ** n) - 1 for between bit n and 0, with the upper bits unchanged
# with the & operation, the upper bits remain unchanged, and the lower bits
# of (2 ** n) & ((2 ** n) - 1) becomes 0
# the net result is bit n is cleared
#
