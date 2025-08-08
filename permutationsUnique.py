# string permutations, all unique characters

# abcdef


# With n for loops, 



def prepend(c, P):
    PP = []
    for s in P:
        s = c + s
        PP.append(s)
    return PP


def permutations(s):
    if len(s) == 1:
        return [s]
    PP = []
    for i in range(len(s)):
        t = s[:i] + s[i + 1:]
        P = permutations(t)
        P = prepend(s[i], P)
        PP += P

    return PP

s = 'abcde'
N = len(s)

P = permutations(s)
print len(P)
print P
