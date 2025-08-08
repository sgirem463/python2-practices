#
# shortest containing substring
#

#
# d is a pattern dictionary
# s is the string
#
def shortestContaining(d, s):
    p = 0
    q = 0
    while q < len(s):
        if s[p] in d:
            d[s[p]] = True
            print 'p:', p, s[p]
            
            






p = 'abcd'

D = {}
for c in p:
    D[c] = False

print D

s = 'President Trump on Monday closed out an us-against-them midterm election campaign that was built on dark themes of fear, nationalism and racial animosity in an effort to salvage Republican control of Congress for the remaining two years of his term'

print s
print 'length:', len(s)

shortestContaining(D, s)






