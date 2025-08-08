def stringRotate(s, n): # string s rotate right by n positions
    print s, n
    slen = len(s)
    if slen == 0:
        return s
    if n == 0:
        return s
    n = n % slen
    s2 = ''
    for i in range(slen):
        s2 += s[(slen - n + i) % slen]
    print s2
    print
    return s2

stringRotate('abcdefg', 2)
stringRotate('abcdefg', 3)
stringRotate('abcdefg', 5)
stringRotate('abcdefg', 0)
s = 'abcdefg'
stringRotate(s, len(s))
stringRotate(s, 0)
stringRotate("", 0)
