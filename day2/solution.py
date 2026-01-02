from math import log10, ceil
from itertools import starmap, chain

line = next(open('input', 'r')).strip()

ranges = [tuple(map(int,range_str.split('-'))) for range_str in line.split(',')]
# sort ranges by start
ranges.sort(key=lambda t: t[0])

# check that ranges are distinct
start, stop = 0, 0
for start, new_stop in ranges:
    assert stop < new_stop
    stop = new_stop

def number_first_half(start):
    return int(start // 10**ceil((log10(start)) / 2))

def candidate_from_part(part):
    return int(str(part)+str(part))

# naive solution
s = 0
for c in range(1, number_first_half(stop)):
    cand = candidate_from_part(c)
    if any(starmap(lambda start, stop: start <= cand <= stop, ranges)):
        s += cand
print("Sum Q1", s)

# naive solution
duplicates = set()
max_exp = ceil(log10(stop))
for inc in range(1, number_first_half(stop)):
    cand = str(inc)
    while len(cand) <= max_exp:
        cand += str(inc)
        # notice the second check to avoid double counting
        if any(starmap(lambda start, stop: start <= int(cand) <= stop, ranges)):
            duplicates.add(int(cand))

print("Sum Q2", sum(duplicates))