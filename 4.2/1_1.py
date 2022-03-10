import queue
from dataclasses import dataclass, field

string = input()
# string = 'abacabad'
queue = queue.PriorityQueue()
dictionary = {}
for letter in string:
    dictionary[letter] = dictionary.get(letter, 0) + 1


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    letter: string = field(compare=False)
    code: string = ''


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


for letter in dictionary:
    queue.put(PrioritizedItem(dictionary[letter], letter))


while queue.qsize() > 1:
    item1 = queue.get()
    item2 = queue.get()
    queue.put(PrioritizedItem(item1.priority + item2.priority, [(item1.letter, '0'), (item2.letter, '1')]))

generate_code(queue.get().letter)
encoded_str = encode(string)

print(len(dictionary), len(encoded_str))
for letter in dictionary.items():
    print('{} {}'.format(letter[0], letter[1]))
print(encoded_str)