#
# GCD(Greatest Common Divisor) of two numbers using recursion
#

def swap(a, b):
    tmp = a
    a = b
    b = tmp

def gcd(p, q):
    if q > p:
        tmp = p
        p = q
        q = tmp

    while q:
        p, q = q, p % q

    return p


def gcd2(p, q):

    if p % q:
        return gcd2(q, p % q)
    else:
        return q



print gcd(24, 16)
print gcd(63, 42)
print gcd(97, 11)
      
print

print gcd2(24, 16)
print gcd2(63, 42)
print gcd2(97, 11)
