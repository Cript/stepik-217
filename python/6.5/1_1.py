from random import randint
from bisect import bisect_left, bisect_right

segments = [
    '6 6',
    '0 3',
    '1 3',
    '2 3',
    '3 4',
    '3 5',
    '3 6',
    '1 2 3 4 5 6'
]
# segments = [
#     '10 5',
#     '0 3',
#     '-2 3',
#     '-1 0',
#     '-1 3',
#     '0 1',
#     '-2 -1',
#     '1 3',
#     '2 3',
#     '1 2',
#     '2 3',
#     '-3 -1 0 2 3'
# ]
# points = [-3, -1, 0, 2, 3]

segments_start = []
segments_end = []

# segments_number, points_number = [int(i) for i in input().split()]
segments_number, points_number = [int(i) for i in segments.pop(0).split()]

for segment in range(0, segments_number):
    # start, end = [int(i) for i in input().split()]
    start, end = [int(i) for i in segments.pop(0).split()]
    segments_start.append(start)
    segments_end.append(end)

# points = [int(i) for i in input().split()]
points = [int(i) for i in segments.pop(0).split()]


def quick_sort(A, l, r):
    if l >= r:
        return

    k = randint(l, r)
    A[k], A[l] = A[l], A[k]
    m, t = partition(A, l, r)
    quick_sort(A, l, m - 1)
    quick_sort(A, t + 1, r)


def partition(A, l, r):
    x = A[l]
    j = l
    i = l
    t = r
    while i <= t:
        if A[i] < x:
            A[j], A[i] = A[i], A[j]
            j += 1
            i += 1
        elif A[i] > x:
            A[i], A[t] = A[t], A[i]
            t -= 1
        else:
            i += 1

    return j, t


# def binary_search(A, k, less_or_equal=True):
#     l = 0
#     n = len(A)
#     r = n
#     m = 0
#     while l < r:
#         m = (r + l) // 2
#         if A[m] == k:
#             if less_or_equal:
#                 while m + 1 < n and A[m + 1] == k:
#                     m += 1
#             else:
#                 while m - 1 >= 0 and A[m - 1] == k:
#                     m -= 1
#                 m -= 1
#             break
#         elif A[m] > k:
#             r = m
#         else:
#             l = m + 1
#
#     while m > -1 and A[m] > k:
#         m -= 1
#
#     return m + 1


quick_sort(segments_start, 0, len(segments_start) - 1)
quick_sort(segments_end, 0, len(segments_end) - 1)

print(segments_start)
print(segments_end)
start_number = bisect_right(segments_start, 3)
end_number = bisect_left(segments_end, 3)
print(start_number)
print(end_number)

result = []

for point in points:
    start_number = bisect_right(segments_start, point)
    end_number = bisect_left(segments_end, point, False)

    result.append(str(start_number - end_number))

print(' '.join(result))
