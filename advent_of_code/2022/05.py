import re

input = [n.rstrip('\n') for n in open("05_input.txt")]
crates = input[:input.index('')-1]
instructions = input[input.index('')+1:]
stack, stack2 = [[],[],[],[],[],[],[],[],[]], [[],[],[],[],[],[],[],[],[]]

def execute_instruction(move, orig, dest, stack, crate_mover=9000):
    if crate_mover == 9000:
        for i in range(move):
            out = stack[orig-1].pop()
            stack[dest-1].append(out)
    else:
        buffer = stack[orig-1][-move:]
        stack[orig-1] = stack[orig-1][:-move]
        [stack[dest-1].append(i) for i in buffer]
    return stack

for i in reversed(crates):
    for j in range(9):
        val = i[1+j*4]
        if val != ' ':
            stack[j].append(i[1+j*4])
            stack2[j].append(i[1+j*4])

for i in instructions:
    match = re.match(r"move (\d+) from (\d+) to (\d+)", i)
    move, orig, dest = int(match.group(1)), int(match.group(2)), int(match.group(3))
    stack = execute_instruction(move, orig, dest, stack)
    stack2 = execute_instruction(move, orig, dest, stack2, 9001)
    
result1, result2 = '', ''
for i in stack:
    result1 += i[-1]

for i in stack2:
    result2 += i[-1]

print(result1)
print(result2)