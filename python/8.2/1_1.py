# Наибольшая возрастающая подпоследовательность. Нахождение всех чисел, входящих в последовательность

from random import randrange

A = [3,6,12,7,9,24,18,3,9,24]
# A = [5,4,3,2,1]
# A = [3,6,7,12]

# A = []
# for i in range(0, 1000):
#     A.append(randrange(10000000000))
#
# print(A)

# n = input()
# A = [int(i) for i in input().split()]

def LISCreateSequence(A, D, prev, ans):
    L = [None for _ in range(ans)]
    k = 0
    for i in range(1, len(D)):
        if D[i] > D[k]:
            k = i

    j = ans - 1
    while k > -1:
        A_k = A[k]
        L[j] = A_k
        j = j - 1
        k = prev[k]

    return L

def LISBottomUp(A):
    D = [None for _ in range(len(A))]
    prev = [None for _ in range(len(A))]
    for i in range(0, len(A)):
        D[i] = 1
        prev[i] = -1

        for j in range(0, i):
            if A[j] < A[i] and A[i] % A[j] == 0 and D[j] + 1 > D[i]:
                D[i] = D[j] + 1
                prev[i] = j

    return LISCreateSequence(A, D, prev, max(D))

print(len(LISBottomUp(A)))
