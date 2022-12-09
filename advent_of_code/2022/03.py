import numpy as np
import string

input = [n.rstrip('\n') for n in open("03_input.txt")]

def get_common(a, b):
    return list(set(a)&set(b))

def get_common_3(a, b, c):
    return list(set(a)&set(b)&set(c))

def get_priority(character):
    if character.islower():
        return ord(character)-96
    else:
        return ord(character)-38

result, result2, counter, buffer = 0, 0, 0, []
for i in input:
    a, b = i[:len(i)//2], i[len(i)//2:]
    common = get_common(a, b)[0]
    result += get_priority(common)

    buffer.append(i)
    counter += 1
    if counter == 3:
        common = get_common_3(buffer[0], buffer[1], buffer[2])
        result2 += get_priority(common[0])
        buffer, counter = [], 0

print(result)
print(result2)