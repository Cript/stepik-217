number_of_objects, capacity = tuple(int(i) for i in input().split(' '))
objects_value = 0
objects = []

for i in range(number_of_objects):
    value, volume = tuple(int(i) for i in input().split(' '))
    objects.append((value, volume, value / volume))

objects.sort(key=lambda object: object[2])

while capacity > 0:
    if len(objects) == 0:
        break
    value, volume, price = objects.pop()

    if volume > capacity:
        portion = capacity / volume
        volume = volume * portion
        value = value * portion

    capacity -= volume
    objects_value += value

print(f"{objects_value:.3f}")