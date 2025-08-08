

# simple permutations

S = {'a', 'b', 'c'}

def permutation(S):
    p = set()

    print S
    
    if len(S) == 1:
        return S
    
    for a in S:
        q = myPrepend(a, permutation(S - {a}))
        p = p.union(q)

    return p
        


#
# S is a set of strings, a is a character
#
def myPrepend(a, S):
    
    T = set()
    if len(S) == 0:
        return {a}
    
    for s in S:
        t = a + s
        T.add(t)
    return T
        
                       
                       
pp = permutation(S)

print pp
