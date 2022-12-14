f = open("06_input.txt", "r")
input = f.readlines()[0]
stack, result1 = [], 0

for i in range(len(input)):
    stack.append(input[i])
    if len(stack) != 4:
        continue
    elif len(set(stack)) == len(stack):
        result1 = i+1
        break
    else:
        stack.pop(0)

print(result1)