# all subsets of a set

import random
import sets



S1 = []
for i in range(5):
    S1.append(str(i))
    


def listSubsets(S):
    global SS
    a = []
    if len(S) == 1:
        a.append(S)
        return a
    a.append(S) # add self
    for i in S:
        k = '-'.join(sorted(list(S - {i})))
        print 'k:', k
        if k not in SS:
            ss = listSubsets(S - {i}) # add each subset that has one less element
        else:
            ss = SS[k]
        a += ss # add each subset that has one less element

    SS['-'.join(sorted(list(S)))] = a
    
    return a



def listSubsets2(S):
    global SS
    SS['-'.join(sorted(S))] = sorted(S)
    if len(S) == 1:
        return
    for m in S:
        T = list(S)
        T.remove(m)
        k = '-'.join(sorted(T))
        if k not in SS:
            listSubsets2(T) # add each subset that has one less element








SS = {}
print S1

listSubsets2(S1)
print 'size: %d' % (len(SS))
print SS.values()


    
