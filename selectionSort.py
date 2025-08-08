list1 = [3,2,5,7,1]
list2 = [1,2,12,4,17,18]

def selectionsort(List):
    n = len(List)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if List[i] > List[j]:
                tmp = List[i]
                List[i] = List[j]
                List[j] = tmp




selectionsort(list1)
print list1
selectionsort(list2)
print list2
