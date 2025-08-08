# insertion sort
list1 = [3,2,5,7,1]
list2 = [1,2,12,4,17,18]

def insertionSort(List):
    n = len(List)

    #
    # starting from the 2nd item, move it to the left to have a sorted list
    #
    for i in range(1, n):
        for j in range(i, 0, -1):
            if List[j] < List[j - 1]:
                tmp = List[j]
                List[j] = List[j - 1]
                List[j - 1] = tmp
            else:
                continue
    





insertionSort(list1)
print list1
insertionSort(list2)
print list2
