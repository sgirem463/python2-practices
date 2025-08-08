# simple permutations

#
# define permutation() to return a list of permutations in string format
#
# then the recursive form of permutation() follows the intuative approach of generating
# permutations: Select 1 of the n items (n choices) as the first item, the next item has n-1 choices ....
#
#
# the permutaion of 1, 2, 3,....n is
# the union of:
#
# 1 followed by permutations of {2, 3....n}
# 2 followed by permutations of (1, 3, 4,...n}
# 3 followed by permutations of {1, 2, 4, ....n}
# ...
# n followed by permutations of {1, 2, ....n-1}
#
#
# This does exhaust all permutations
#

K = ['a', 'b', 'c', 'd']

def permutation(L):
    p = []

    print '-', L
    
    if len(L) == 1:
        return L
    
    for a in L:
        L1 = list(L)
        L1.remove(a)
        print '=', L1
        q = myPrepend(a, permutation(L1))
        p += q

    return p
        


#
# S is a set of strings, a is a character
#
def myPrepend(a, L):
    
    LL = []
    if len(L) == 0:
        return [a]
    
    for s in L:
        t = a + s
        LL.append(t)
    return LL
        
                       
                       
pp = permutation(K)

print pp, len(pp)
