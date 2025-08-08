#
# iterative approach for permutations
#


#
# set P to have an empty string to begin with for the current algorithm,
# or set P to equal to L for when it's empty
# if len(P) == 0:
#     PP = L
#
P = ['']


def permutations(L):
    global P
    
    for i in range(len(L)): # string length grow by 1 for each iteration 
        permu(L)


def permu(L):
    global P

    PP = []

    for s in P:
        for a in L:
            if a not in s: # string can use the "in" function
                PP.append(s + a)

    P = PP


K = ['a', 'b', 'c']

permutations(K)

print P
            
