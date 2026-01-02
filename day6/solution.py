import io
from math import prod

input = open('input','r')
test_input = io.StringIO("""123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """)

lines = [line.split() for line in input]
operator_line = lines.pop()
lines = [[int(v) for v in line] for line in lines]

operator_mapping = {
    '+': sum,
    '*': prod
}

operators = [operator_mapping[k] for k in operator_line]
# transform to polish
nums = zip(operators,*lines)
results = map(lambda l: l[0](l[1:]), nums)
print("Q1", sum(results))

input = open('input','r')
test_input = io.StringIO("""123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
                    """)

lines = [list(line) for line in input][:5]

def get_column(li):
    return [l.pop() for l in li]

numbers = []
results = []
# remove first empty line
get_column(lines)
while True:
  col = get_column(lines)
  potential_operator = col.pop().strip()
  numbers.append(int(''.join(col)))
  if potential_operator: 
    if potential_operator == '+':
        op = sum
    elif potential_operator == '*':
        op = prod
    else:
       print(potential_operator)
    results.append(op(numbers))
    if len(lines[0]) == 0:
     break
    get_column(lines)
    numbers = []

print("Q2", sum(results))