import io

input = open('input','r')
input = io.StringIO("""[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
""")

def parse_machine(line):
    button_substr = line[line.index('[') + 1: line.index(']')]
    switches_substr = line[line.index(']') + 2: line.index('{') - 1].replace(' ', ',')
    joltage_substr = line[line.index('{') + 1: line.index('}')]
    button_target = [1 if c == '#' else 0 for c in button_substr]
    # absolutely horrible, but works
    switches_tuple = eval('('+switches_substr.replace(')', ',)')+')')
    switches_effect = [[1 if i in switch_indx else 0 for i in range(len(button_target))] for switch_indx in switches_tuple]
    joltage = list(map(int, joltage_substr.split(',')))
    return {
        'target': button_target,
        'switches': switches_effect,
        'joltage': joltage
    }

def solve_machine(machine):
    target = machine.target
    switches = machine.switches


machines = list(map(parse_machine, input))
print(machines)