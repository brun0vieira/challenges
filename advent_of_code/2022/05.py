import re
import os
from time import sleep

input = [n.rstrip('\n') for n in open("05_input.txt")]
crates = input[:input.index('')-1]
instructions = input[input.index('')+1:]
stack = [[],[],[],[],[],[],[],[],[]]

def execute_instruction(move, orig, dest, stack):
    for i in range(move):
        out = stack[orig-1].pop()
        stack[dest-1].append(out)

for i in reversed(crates):
    for j in range(9):
        val = i[1+j*4]
        if val != ' ':
            stack[j].append(i[1+j*4])

for i in instructions:
    match = re.match(r"move (\d+) from (\d+) to (\d+)", i)
    move, orig, dest = int(match.group(1)), int(match.group(2)), int(match.group(3))
    execute_instruction(move, orig, dest, stack)

result = ''
for i in stack:
    result += i[-1]

print(result)