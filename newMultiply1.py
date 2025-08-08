# multiply without *, recursive


def newMultiply(a, b, position):
    if position == 0:
        if (1 & b):
            return a
        else:
            return 0

    if ((1 << position) & b):
        return (a << position) + newMultiply(a, b, position - 1)
    else:
        return newMultiply(a, b, position - 1)


print newMultiply(4, 5, 63)
