# Наибольшая возрастающая подпоследовательность. O(nlog(n))

import math
from bisect import bisect_right

A = [1,9,5,7,3]
# A = [5,4,3,2,1]
# A = [32,27,74,20,27,34,7,41,65,66,19,75,58,38,49,85,4,50]

def LISBottomUp(A):
    n = len(A)
    D = [math.inf] * (n + 1)
    D[0] = -math.inf
    for i in range(n):
        for j in range(1, n + 1):
            # print(D)
            if D[j - 1] < A[i] and A[i] < D[j]:
                D[j] = A[i]
        # D[i] += 1

    print(D)

    # ans = 0
    # for i in range(1, len(A)):
    #     ans = max(ans, D[i])


LISBottomUp(A)
