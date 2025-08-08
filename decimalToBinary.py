#
# convert a decimal number to binary using recursive algorithm
#

def decimalToBinary(dec):
    if dec == 0:
        return '0'
    elif dec == 1:
        return '1'
    else:
        return (decimalToBinary(dec >> 1) + str(dec & 0x1))



def decimalToBinary2(dec):
    #
    # print the binary digit in each recursive routine
    # bits in higher position should be printed before bits in lower positions
    # therefore we should have a print statement after the recursive function
    # call
    #
    if dec > 1:
        decimalToBinary2(dec // 2)
    print (dec % 2),





def powerOfNumber(n, p):
    if p == 0:
        return 1
    else:
        return n * powerOfNumber(n, p - 1)





print decimalToBinary(7)
print decimalToBinary(12)
print decimalToBinary(39)
print decimalToBinary(123)

print

decimalToBinary2(7)
print
decimalToBinary2(12)
print
decimalToBinary2(39)
print
decimalToBinary2(123)
print

print powerOfNumber(2, 4)
print powerOfNumber(3, 3)
print powerOfNumber(5, 4)
print powerOfNumber(2, 0)


