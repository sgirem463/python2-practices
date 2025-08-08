

#
# 10*11*01

def printStrings(s, n):

    if n == (len(s) - 1):
        print s
        return

    if s[n] == '*':
        printStrings(s[:n] + '0' + s[n+1:], n+1)
        printStrings(s[:n] + '1' + s[n+1:], n+1)
    else:
        printStrings(s, n+1)



s = '10*11*01'
printStrings(s, 0)


printStrings('0*1*0', 0)
