# Наибольшая возрастающая подпоследовательность. Нахождение ТОЛЬКО длины

A = [3,2,1,4,5]
# A = [5,4,3,2,1]


def LISBottomUp(A):
    D = [None for _ in range(len(A))]
    for i in range(0, len(A)):
        D[i] = 1

        for j in range(0, i):
            if A[j] < A[i] and D[j] + 1 > D[i]:
                D[i] = D[j] + 1

    print(D)

    # ans = 0
    # for i in range(1, len(A)):
    #     ans = max(ans, D[i])
    # return ans


print(LISBottomUp(A))
