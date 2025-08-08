
results = []


#
# The first solution uses iterative (through each character) approach, grow(double the size) the existing
# result set by duplicating each string then have the specific position replaced with the altenate character
#
def suggest(name):
    for i in range(len(name)):
        print name[i]
        if name[i] == 'o':
            replicate(i, '0')
        if name[i] == 'h':
            replicate(i, '7')        


def replicate(n, c):
    global results
    
    r = list(results)
    for s in results:
        r.append(s[:n] + c + s[n+1:])
    results = list(r)
    print results



#
# The second aolution works out my original recursive approch, it's more sophisticated
# but also more complicated and harder to get completely right.
#
# The 2nd approach might not be easy to complete in the interview, but it hard
# not for me to feel a little unhappy about myself not to come up with the first iterative approach
#

def suggest2(s):

    print 's:', s
    if s == '':
        return[]
    r = []
    if s[0] == 'o':
        r += prepend('0', suggest2(s[1:]))
        r += prepend('o', suggest2(s[1:]))
    elif s[0] == 'h':
        r += prepend('h', suggest2(s[1:]))
        r += prepend('7', suggest2(s[1:]))
    else:
        r += prepend(s[0], suggest2(s[1:]))
    return r


def prepend(s1, L):
    print 'L:', L
    if L == []:
        return [s1]
    LL = []
    for s in L:
        LL.append(s1 + s)
    return LL


print '--- using suggest ---'
name = 'john'
results.append(name)
suggest(name)
results.remove(name)
print results
print

print '--- using suggest 2 ---'
results = suggest2(name)
results.remove(name)
print results



