#
# Binary evaluation
#

# countEval("1^0|0|1", False)
# countEval("0&0&0&1^1|1", True)
# countEval("0^0&0^1|1", True)
#


def countEval(s, result):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        if int(s[0]) == 1:
            if result:
                return 1
            else:
                return 0
        else:
            if result:
                return 0
            else:
                return 1

    totalCount = 0;
    for i in range(1, len(s), 2):
        count = 0

        if s[i] == '&':
            if result:
                count = countEval(s[:i], True) * countEval(s[i+1:], True)
            else:
                count = countEval(s[:i], True) * countEval(s[i+1:], False)
                count += countEval(s[:i], False) * countEval(s[i+1:], True)
                count += countEval(s[:i], False) * countEval(s[i+1:], False)
                
        elif s[i] == '|':
            if result:
                count = countEval(s[:i], True) * countEval(s[i+1:], True)
                count += countEval(s[:i], True) * countEval(s[i+1:], False)
                count += countEval(s[:i], False) * countEval(s[i+1:], True)
            else:
                count = countEval(s[:i], False) * countEval(s[i+1:], False)
        elif s[i] == '^':
            if result:
                count = countEval(s[:i], True) * countEval(s[i+1:], False)
                count += countEval(s[:i], False) * countEval(s[i+1:], True)
            else:
                count = countEval(s[:i], True) * countEval(s[i+1:], True)
                count += countEval(s[:i], False) * countEval(s[i+1:], False)

        totalCount += count

    return totalCount



print countEval("1^0|0|1", False)
print
print countEval("0&0&0&1^1|0", True)
print
print countEval("0^0&0^1|1", True)

                  
