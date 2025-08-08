# Palindrome Permutation

s = 'Tact Coa'
print s

s = s.lower()

L = list(s)
print L

# either all or all but one characters' count are even

# ideally a hash table to keep the count
# use a dictionary should be okay

oddCount = 0

D = {}

for c in L:
    if c == ' ':
        continue
    if c not in D:
        D[c] = 1
        oddCount += 1
    else:
        D[c] += 1
        if (D[c] % 2 == 1):
            oddCount += 1
        else:
            oddCount -= 1

print D
print oddCount
if (oddCount > 1):
    print s, 'is not a palindrome'
else:
    print s, 'is a palindrome'
