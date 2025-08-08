#
# median of a stream
#

import heapq

def printMedian(S):

    L = []
    H = []

    for value in S:
        if len(H) == 0:
            heapq.heappush(H, value)
        elif value >= H[0]:
            heapq.heappush(H, value)
        else:
            heapq.heappush(L, -value)
            
        if (len(H) - len(L)) > 1:
            heapq.heappush(L, -heapq.heappop(H))

        if (len(L) - len(H)) > 1:
            heapq.heappush(H, -heapq.heappop(L))

        if len(L) > len(H):
            print -L[0]
        elif len(L) < len(H):
            print H[0]
        else:
            print (H[0] - L[0])/2
            
           

    

printMedian([5, 15, 1, 3])
