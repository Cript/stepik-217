string = input()
# string = 'abacabad'
# string = 'abc'
queue = []
dictionary = {}
for letter in string:
    dictionary[letter] = dictionary.get(letter, 0) + 1

for letter in dictionary:
    queue.append((dictionary[letter], letter))


def sort_queue(queue):
    return sorted(queue, key=lambda letter: letter[0])


def generate_code(tree, code = ''):
    while len(tree) > 0:
        left = tree.pop(0)
        right = tree.pop(0)

        if isinstance(left[0], str):
            dictionary[left[0]] = code + left[1]
        else:
            generate_code(left[0], code + left[1])


        if isinstance(right[0], str):
            dictionary[right[0]] = code + right[1]
        else:
            generate_code(right[0], code + right[1])


def encode(string):
    encoded_str = ''
    for letter in string:
        encoded_str += dictionary[letter]
    return encoded_str


queue = sort_queue(queue)

for k in range(len(dictionary), 2*len(dictionary) - 1):
    item1 = queue.pop(0)
    item2 = queue.pop(0)
    queue.append((item1[0] + item2[0], [(item1[1], '0'), (item2[1], '1')]))
    queue = sort_queue(queue)

if len(dictionary) <= 2:
    for index, key in enumerate(dictionary):
        dictionary[key] = str(index)
else:
    generate_code(queue.pop(0)[1])

encoded_str = encode(string)

print(len(dictionary), len(encoded_str))
for letter in dictionary.items():
    print('{} {}'.format(letter[0], letter[1]))
print(encoded_str)
