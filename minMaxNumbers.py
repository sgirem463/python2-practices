#
# smallest and largest number in an array of numbers
#

L = [45, 34, 21, 28, 3, 11, 7, 89, 73, 44, 27, 15, 98, 66, 70]

def smallestLargest(L):

    s = L[0]
    l = L[0]

    for num in L[1:]:
        if num < s:
            s = num

        if num > l:
            l = num

    return (s, l)


print smallestLargest(L)
