lines = [line.rstrip() for line in open('input','r')]

def joltage_for_line(line):
    numbers = [int(i) for i in list(line)]
    first = 0
    second = 0
    for i in range(len(numbers)-1):
        if numbers[i] > first:
            first = numbers[i]
            second = numbers[i+1]
        if numbers[i+1] > second:
            second = numbers[i+1]
    return 10 * first + second


print("Q1", sum(map(joltage_for_line, lines)))

def joltage2_for_line(line):
    numbers = [int(i) for i in list(line)]
    relevants = [0 for _ in range(12)]
    for i in range(len(numbers)-11):
        for j in range(12):
            if numbers[i + j] > relevants[j]:
                for k in range(j, 12):
                    relevants[k] = numbers[i+k]
    sum = 0
    for i in range(12):
        sum += 10**(11-i) * relevants[i]
    return sum


print("Q2", sum(map(joltage2_for_line, lines)))
