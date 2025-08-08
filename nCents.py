# n cents with quarters, dimes, nickels, cents

def nCents(n):
    for i in range(0, n / 25 + 1):
        for j in range(0, (n - (i * 25)) / 10 + 1):
            for k in range(0, (n - (i * 25) - (j * 10)) / 5 + 1):
                l = n - (i * 25) - (j * 10) - (k * 5)
                print [i, j, k, l]


nCents(36)


def nCents2(n):
    for i in range(0, n / 25 + 1):
        for j in range(0, (n - (i * 25)) / 10 + 1):
            for k in range(0, (n - (i * 25) - (j * 10)) / 5 + 1):
                nCents2(n - (i * 25) - (j * 10) - (k * 5))
                print [i, j, k, l]
