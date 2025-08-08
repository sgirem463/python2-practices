#
#
# flip to win
#
import sys

def findLongest(n):
    long1 = 0
    longest = 0
    for i in range(64):
        if (1 << i) & n != 0:
            long1 += 1
        else:
            longest = max(longest, long1)
            long1 = 0

    longest = max(longest, long1)
    return longest

#
# brute force
#
def flipToWin(n):
    longest = 0
    longest = findLongest(n) # when there is no 0 in the binary representation
    for i in range(64):
        if (n >> i) & 1 == 0:
            n1 = (1 << i) | n
            long1 = findLongest(n1)
            longest = max(longest, long1)

    print longest
    return longest




#
# one walk, optimal solution
#
def flipToWin2(n):
    zeroCount = 0
    long1 = 0
    long2 = 0
    longest = 0

    for i in range(64):
        if (1 << i) & n != 0:
            if zeroCount == 0:
                long1 += 1
                long2 += 1
#                print 'a', long1, long2

            elif zeroCount == 1:
                zeroCount = 0
                long2 = long2 + 1 + 1 
                long1 = 1
#                print 'b', long1, long2


            else:
                zeroCount = 0
                long1 = 1
                long2 = 2
#                print 'c', long1, long2


        else:
            if zeroCount == 0:
                zeroCount = 1
                longest = max(longest, long2)
                long2 = long1
                long1 = 0
#                print 'd', long1, long2


            elif zeroCount == 1:
                zeroCount = 2
                longest = max(longest, long2)

                long2 = 0
#                print 'e', long1, long2

            else:
                zeroCount += 1
#                print 'f', long1, long2

                
            
    longest = max(longest, long2)
    print longest
    return longest






flipToWin(0b10110110011111011110101110111011101111110110)

flipToWin(0b11101111)
flipToWin(0b1100011000000001110111)
flipToWin(0b11110010111001101101)
flipToWin(0b10111011101111110110)
flipToWin(0b100000000)
flipToWin(0b11110010111001101100)
flipToWin(0b010101110011001111001110010010111101010011101011011)
flipToWin(0b111111111111)
flipToWin(0b111111111111110)
flipToWin(0b11111111111111110)
flipToWin(0b11111111011111111)
flipToWin(0b11111111111111111)


print

flipToWin2(0b10110110011111011110101110111011101111110110)
#sys.exit(0)

flipToWin2(0b11101111)
flipToWin2(0b1100011000000001110111)
flipToWin2(0b11110010111001101101)
flipToWin2(0b10111011101111110110)
flipToWin2(0b100000000)
flipToWin2(0b11110010111001101100)
flipToWin2(0b010101110011001111001110010010111101010011101011011)
flipToWin2(0b111111111111)
flipToWin2(0b111111111111110)
flipToWin2(0b11111111111111110)
flipToWin2(0b11111111011111111)
flipToWin2(0b11111111111111111)


