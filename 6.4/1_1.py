input_elements_number = 5
input_elements_string = '2 3 9 2 9'

# input_elements_number = input()
input_elements = [int(i) for i in input_elements_string.split()]
# input_elements = [int(i) for i in input().split()]
number_of_inversions = 0


def merge_sort(l, r):
    if l < r:
        m = (l + r) // 2
        result = merge(merge_sort(l, m), merge_sort(m + 1, r))
        # print('merge_sort', result)
        return result

    return [input_elements[l]]


def merge(left, right):
    global number_of_inversions
    left_count = len(left)
    right_count = len(right)
    result = []
    # print('merge', left, right)
    while left_count != 0 or right_count != 0:
        # print('merge result', result)
        if left_count == 0:
            result += right
            return result

        if right_count == 0:
            result += left
            return result

        if left[0] <= right[0]:
            result.append(left[0])
            left_count -= 1
            del left[0]
            continue
        else:
            number_of_inversions += len(left)
            result.append(right[0])
            right_count -= 1
            del right[0]
            # print(result)
            continue


# print(merge_sort(0, len(input_elements) - 1))
merge_sort(0, len(input_elements) - 1)
print(number_of_inversions)
