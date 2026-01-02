input = open('input','r')
input_test = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""".split()

def pretty_print(arr):
    print("\n".join(["".join([str(i) for i in line]) for line in arr]))


lines = [[1 if c == '@' else 0 for c in list(line.rstrip())] for line in input]
# add zero row on top
lines = [[0 for _ in lines[0]]] + lines + [[0 for _ in lines[0]]]
# add zeros left and right
lines = [[0] + line + [0] for line in lines]

def neighbour_sum(current_state):
    neighbour_sum = [[9 for _ in current_state[0]] for _ in current_state]
    for i in range(1, len(current_state) - 1):
        for j in range(1, len(current_state[i]) - 1):
            if current_state[i][j]:
                neighbour_sum[i][j] = 0
                for i1 in range(-1, 2, 1):
                    for j1 in range(-1, 2, 1):
                        if i1 == 0 and j1 == 0:
                            continue
                        neighbour_sum[i][j] += current_state[i+i1][j+j1]
    return neighbour_sum

below4perline = [len(list(filter(lambda x: x < 4, line))) for line in neighbour_sum(lines)]
total = sum(below4perline)
print("Q1", total)

def remove(state):
    nsum = neighbour_sum(state)
    rem_count = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if nsum[i][j] < 4:
                state[i][j] = 0
                rem_count += 1
    return state, rem_count


state = lines
removed_all = []
while True:
    state, removed = remove(state)
    removed_all.append(removed)
    if removed == 0:
        break

print("Q2", sum(removed_all))