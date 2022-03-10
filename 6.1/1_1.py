input_elements_string = '5 1 5 8 12 13'
input_keys_string = '5 8 1 23 1 11'

A = input().split()
A = [int(i) for i in input().split()]
A.pop(0)

# input_keys = input().split()
input_keys = [int(i) for i in input().split()]
input_keys.pop(0)

keys = []

def binary_search(A, k):
    l = 0
    r = len(A) - 1
    while l <= r:
        m = int(l + (r - l) / 2)
        if A[m] == k:
            return m
        elif k < A[m]:
            r = m - 1
        else:
            l = m + 1
    return -2


for key in input_keys:
    keys.append(str(binary_search(A, key) + 1))

print(' '.join(keys))
