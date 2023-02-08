# Наибольшая возрастающая подпоследовательность. Нахождение всех чисел, входящих в последовательность

A = [3,2,3,4,5]
# A = [5,4,3,2,1]

def LISCreateSequence(A, D, prev, ans):
    L = [None for _ in range(ans)]
    k = 0
    for i in range(1, len(D)):
        if D[i] > D[k]:
            k = i

    j = ans - 1
    while k > -1:
        L[j] = A[k]
        j -= 1
        k = prev[k]

    return L

def LISBottomUp(A):
    D = [None for _ in range(len(A))]
    prev = [None for _ in range(len(A))]
    for i in range(0, len(A)):
        D[i] = 1
        prev[i] = -1

        for j in range(0, i):
            if A[j] < A[i] and D[j] + 1 > D[i]:
                D[i] = D[j] + 1
                prev[i] = j

    ans = 0
    for i in range(1, len(A)):
        ans = max(ans, D[i])

    return LISCreateSequence(A, D, prev, ans)

print(LISBottomUp(A))
