# read the file, iterate over lines
# left is negative, right is positive rotations
# accumulate to get the net shift of all moves
# we mod by 100 to eliminate full turns. If the result is 50 the dial is on zero
# count such cases
from itertools import accumulate, pairwise, starmap

rotations = [int(line.rstrip().replace('L', '-').replace('R','+')) for line in open('input','r')]

print("Q1", len([i for i in accumulate(rotations) if i % 100 == 50]))

def zero_crossing(start,stop):
    full_turns = abs(start // 100 - stop // 100)
    # // is asymmetric in nature, we need to correct two cases
    # we come from above and end on zero - this would not count above but should count
    correction_1 = 1 if stop % 100 == 0 and stop <= start else 0
    # we start on a zero and go further below - this should _not_ count
    correction_2 = -1 if start % 100 == 0 and stop < start else 0
    return full_turns + correction_1 + correction_2

final_position = map(lambda i: i + 50, accumulate(rotations))
print("Q2", sum(starmap(zero_crossing, pairwise(final_position))))