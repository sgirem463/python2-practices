#
# factorial of a number
#

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def factorial2(n):
    f = 1
    for i in range(n, 0, -1):
        f = i * f

    return f



print factorial(3)
print factorial(4)
print factorial(5)
print factorial(6)

print factorial2(3)
print factorial2(4)
print factorial2(5)
print factorial2(6)
