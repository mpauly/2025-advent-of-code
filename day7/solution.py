import io

input = open('input','r')
test_input = io.StringIO(""".......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............""")


lines = [list(line.strip()) for line in input]
initial_tachyon = lines.pop(0).index('S')
tachyons_at = set([initial_tachyon])
splits = 0
for line in lines:
    incoming_beam = list(tachyons_at)
    for beam in incoming_beam:
        if line[beam] == '^':
            splits += 1
            tachyons_at.remove(beam)
            tachyons_at.add(beam - 1)
            tachyons_at.add(beam + 1)
print("Q1", splits)

ways_to_get_to = [[0 for _l in lines[0]]]
ways_to_get_to[0][initial_tachyon] = 1

for prev_line, line in enumerate(lines):
    new_line = ways_to_get_to[prev_line].copy()
    for char_id, char in enumerate(line):
        if char == '^':
            new_line[char_id] = 0
            new_line[char_id-1] += ways_to_get_to[prev_line][char_id]
            new_line[char_id+1] += ways_to_get_to[prev_line][char_id]
    ways_to_get_to.append(new_line)

print("Q2", sum(ways_to_get_to[-1]))