# boolean evaluations
# 0, 1, and, or, xor
#
# 1 ^ 0 | 0 | 1 , false -> 2
# 0 & 0 & 0 & 1 ^ 1 | 0 , true -> 10
#

# Representations, and end of operations

# (1 ^ 0) | 0 | 1
# 1 ^ (0 | 0) | 1
# 1 ^ 0 | (0 | 1)
# (1 ^ 0 | 0) | 1
# 1 ^ (0 | 0 | 1)
# (1 ^ 0 | 0 | 1)

# (1 ^ 0) | (0 | 1)

# when there are only 1 or 2 components left, the operation ends

# ease of representations first
# ((1, 2), 3), 4)
# (1,2,3,4)
# (1, 2), 3, 4
# use python list


def booleanEvaluation(L):
    for i in range(len(L) - 1):
        for j in range(i + 1, len(L) - 1):

            B = []
            for k in range(i, j + 1):
                B.append(L[k])

            T = tuple(B)

            C = L[0: i]
            C.append(T)
            
            D = C + L[j + 1:]
            T = tuple(D)
#            DD[T] = 1

            
            if T in DD:
                continue


            if T not in DD:
                DD[T] = booleanEvaluation(C + L[j + 1:])
            





DD = {}
