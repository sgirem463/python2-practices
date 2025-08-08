import random



A = [random.randrange(100)  for i in range(30)]

print A
print



def peakValley(L):
    size = len(L)

    for i in range(1, size, 2):
        largest = i
        if L[largest] < L[i-1]:
            largest = i - 1
        if i < size - 1:
            if L[largest] < L[i+1]:
                largest = i + 1
        if largest == i:
            continue
        tmp = L[i]
        L[i] = L[largest]
        L[largest] = tmp


peakValley(A)
print
print A
