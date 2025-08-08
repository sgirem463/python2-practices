

import heapq
#
# T = int(input())
# for _ in range(T):
#    k, n = [int(x) for x in input().strip().split(' ')]
#    arr = [int(x) for x in input().strip().split(' ')]


def kthLargest(arr, k, n):
    h = []
    for i in range(k-1):
        h.append(arr[i])
        print(-1)
    
    h.append(arr[k-1])
    heapq.heapify(h)
    print(h[0])
    
    for i in range(k, n):
        heapq.heappushpop(h, arr[i])
        print(h[0])
    
    print()


kthLargest([1, 2, 3, 4, 5, 6], 4, 6)
