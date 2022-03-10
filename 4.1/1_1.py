number_of_segments = int(input())
segments = []
points = []
for i in range(number_of_segments):
    segments.append(tuple(int(i) for i in input().split(' ')))
segments.sort(key=lambda segment: segment[1])

while len(segments) > 0:
    point = segments[0][1]
    points.append(str(point))
    segments = list(filter(lambda segment: segment[0] > point, segments))

print(len(points))
print(' '.join(points))