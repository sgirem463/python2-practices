L1 = [7,1,6]
L2 = [5,9,2,5,8]
len1 = len(L1)
len2 = len(L2)

sum = 0
if len1 == len2:
    for i in range(len1):
        sum += (L1[i] + L2[i]) * (10 ** i)

    print sum

if (len1 < len2):
    for i in range(len2):
        if (i + 1) > len1:
            sum += L2[i] * (10 ** i)
        else:
            sum += (L1[i] + L2[i]) * (10 ** i)

    print sum
        

# C can use similar idea, but needs a more sophisticetaed mechanism
# to detect which list has already run out, may not be too bad
