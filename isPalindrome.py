
s1 = 'taco cat'
s2 = 'another string'


# singly linked list
# in C, reverse the linked list, record the size and compare the
# two lists


def isPalindrome(s):
    print s
    size = len(s)
    if size == 0:
        return True

    L1 = list(s)
    while ' ' in L1:
        L1.remove(' ')

    print L1
    L2 = L1[::-1]
    print L2
    L3 = [i for i in reversed(L1)]
    print L3

    for i in range(size / 2):
        if (L1[i] != L2[i]):
            return False
    return True

if __name__ == '__main__':
    print isPalindrome(s1)
    print
    print isPalindrome(s2)

