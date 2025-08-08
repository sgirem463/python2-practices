L = [3,5,8,5,10,2,1]

print L

BIGGER = []
SMALLER = []
XLIST = []
x = 5

for i in L:
    if i < x:
        SMALLER.append(i)
    elif i > x:
        BIGGER.append(i)
    else:
        XLIST.append(i)

M = SMALLER + XLIST + BIGGER
print M

# C can use 3 lists to do the same thing, need to make sure the pointers
# are delinked and linked properly
