import math

# number_operations = input()
# operations = []
operations = ['Insert 10', 'Insert 200', 'ExtractMax', 'Insert 5', 'Insert 500', 'ExtractMax']
tree = []
maximums = []

# for i in range(int(number_operations)):
#     operations.append(input())


def execute_operation(operation):
    if operation[0] == 'Insert':
        insert(operation[1])
    elif operation[0] == 'ExtractMax':
        extract_max()


def move_up(key):
    if key == 0:
        return

    value = tree[key]
    parent_key = math.floor((key - 1) / 2)
    parent_value = tree[parent_key]
    if value > parent_value:
        tree[parent_key], tree[key] = tree[key], tree[parent_key]
        move_up(parent_key)


def move_down(key):
    # print(1, key, len(tree), tree)

    left_children_key = (key + 1) * 2 - 1
    right_children_key = (key + 1) * 2

    if len(tree) < left_children_key + 1:
        return

    # print(2, left_children_key, right_children_key)

    left_children = tree[left_children_key]
    right_children = None

    if len(tree) > right_children_key:
        right_children = tree[right_children_key]

    max_children_key = left_children_key
    if right_children is not None and right_children > left_children:
        max_children_key = right_children_key

    if tree[max_children_key] > tree[key]:
        tree[key], tree[max_children_key] = tree[max_children_key], tree[key]
        move_down(max_children_key)

    # print(3, left_children, right_children, max_children_key)


def insert(value):
    # print('insert start', value, tree)
    tree.append(int(value))
    key = len(tree) - 1
    move_up(key)
    # print('insert end', value, tree)


def extract_max():
    if not tree:
        return

    # print('extract_max start', tree)
    maximums.append(tree.pop(0))
    if len(tree) < 2:
        return
    tree.insert(0, tree.pop())
    move_down(0)
    # print('extract_max stop', tree)


for operation_type in operations:
    execute_operation(operation_type.split())

for maximum in maximums:
    print(maximum)

