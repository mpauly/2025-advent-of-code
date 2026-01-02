import io
from itertools import starmap
from functools import reduce

input = open('input','r')

test_input = io.StringIO("""3-5
10-14
16-20
12-18

1
5
8
11
17
32""")

ranges_lines = []
ingredient_lines = []

while line := input.readline():
    if '-' in line:
        ranges_lines.append(line.rstrip())
    elif line.rstrip():
        ingredient_lines.append(line.rstrip())

ranges = [(int(p[0]), int(p[1])) for p in [line.split('-') for line in ranges_lines]]
ingredients = [int(l) for l in ingredient_lines]


availability = [1 if any(starmap(lambda start, stop: start <= ingredient <= stop, ranges)) else 0 for ingredient in ingredients]
print("Q1", sum(availability))

def multirange_add_interval(multirange, interval):
    final = []
    overlapping = []
    for r in multirange:
        if r[1] < interval[0]:
            final.append(r)
        elif r[0] > interval[1]:
            final.append(r)
        else:
            overlapping.append(r)
    final.append((
        min([interval[0]]+[i[0] for i in overlapping]),
        max([interval[1]]+[i[1] for i in overlapping])
    ))
    final.sort(key=lambda t: t[0])
    return final

def items(multirange):
    return reduce(lambda s, t: s + t[1]-t[0]+1, multirange, 0)

multir = reduce(multirange_add_interval, ranges, [])

print("Q2", items(multir))