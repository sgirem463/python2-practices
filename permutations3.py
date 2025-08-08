#
# permutation of all unique characters
#

# [a, b, c]: abc, acb, bac, bca, cab, cba
#

def prepend(c, L):
    print 'c, L:', c, L
    LL = []
    for s in L:
        LL.append(c + s)

    print LL
    return LL

def permutations(s):
    print 's:', s
    SS = []
    if len(s) == 1:
        return [s]
    for c in s:
        s2 = s.replace(c, '')
        SS += prepend(c, permutations(s2))

    return SS


print
        
print permutations('abc')
