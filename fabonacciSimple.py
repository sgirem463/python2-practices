

def fabonacci(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fabonacci(n - 1) + fabonacci(n - 2)



print fabonacci(1)
print fabonacci(2)
print fabonacci(3)
print fabonacci(4)
print fabonacci(5)
print fabonacci(6)
print fabonacci(7)
print fabonacci(8)
print fabonacci(9)
print fabonacci(10)
print fabonacci(11)
print fabonacci(12)


def fabo2(n):
    n1 = 1
    print n1,
    if n == 0:
        return
    n2 = 1
    print n2,
    if n == 1:
        return
    for i in range(2, n + 1):
        tmp = n2
        n2 = n2 + n1
        n1 = tmp
        print n2,
    print

fabo2(15)


def fabo3(n):
    global F
    if n == 0:
        F[0] = 1
    elif n == 1:
        F[1] = 1
    elif not F[n]:
        if not F[n - 1]:
            F[n - 1] = fabo3(n - 1)
        if not F[n - 2]:
            F[n - 2] = fabo3(n - 2)
        F[n] = F[n - 1] + F[n - 2]
    return F[n]


F = []
for i in range(100):
    F.append(None)

print fabo3(15)
print fabo3(5)

F = []
for i in range(100):
    F.append(None)

F[0] = 0
F[1] = 1
def fabo4(n):
    if n <= 0:
        return F[0]
    if n == 1:
        return F[1]
    if not F[n]:
        F[n] = fabo4(n - 1) + fabo4(n - 2)
    return F[n]
    

print fabo4(10)
print fabo4(15)
