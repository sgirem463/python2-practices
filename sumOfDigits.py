#
# sum of digits
#

def sumOfDigits(number):

    if number < 10:
        return number
    lsd = number % 10
    return lsd + sumOfDigits(number // 10)


print sumOfDigits(123)
print sumOfDigits(456)
print sumOfDigits(7230)

