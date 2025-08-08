
list1 = [3,2,5,7,1]
list2 = [1,2,12,4,17,18]

def bubblesort(List):
    n = len(List)

    #
    # n - 1 times, after moving n - 1 smaller values to the front,
    # the last one is guaranteed to be the largest
    #
    for i in range(n - 1):
        #
        # each time, always start from the bottom, compare and swaping as needed
        # all the way to the one that before the last unsorted value
        #
        # item i is still not in the sorted list (or sorted portion)
        #
        for j in range(n - 1, i, -1):
            if (List[j] < List[j-1]):
                tmp = List[j]
                List[j] = List[j-1]
                List[j-1] = tmp


bubblesort(list1)
print list1
bubblesort(list2)
print list2


def bubblesort2(List):
    n = len(List)

    for i in range(n - 1): # has n items, do it n - 1 times
        for j in range(n - i - 1):
            if List[j] > List[j + 1]:
                tmp = List[j]
                List[j] = List[j + 1]
                List[j + 1] = tmp
            

list1 = [3,2,5,7,1]
list2 = [1,2,12,4,17,18]

bubblesort2(list1)
print list1
bubblesort2(list2)
print list2
