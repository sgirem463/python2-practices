#flip to win

def flipToWin(n):
    print '{0:b}'.format(n)
    seenZero = False
    oneCount = 0
    preList = 0
    longest = 0
    for i in range(64):
        if ((1 << i) & n):
            if (not seenZero):
                oneCount += 1
                preList += 1
            else:
                oneCount += 1
                preList += 1
        else:
            if (seenZero):
                if (preList > longest):
                    longest = preList
                    print 'longest: {0:d}'.format(longest)
                    
                preList = oneCount + 1
                oneCount = 0
            else:
                seenZero = True
                preList += 1
                oneCount = 0

    print 'longest: {0:d}'.format(longest)
    print
            

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



'''

oneCount

10110110011111011110101110111011101111110110

11101111

1100011000000001110111

11110010111001101101

10111011101111110110

11110010111001101100

'''
