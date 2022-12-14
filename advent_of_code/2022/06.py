f = open("06_input.txt", "r")
input = f.readlines()[0]
stack = []

def get_marker(part1=True):
    nr = 4 if part1 else 14   
    for i in range(len(input)):
        stack.append(input[i])
        if len(stack) != nr:
            continue
        elif len(set(stack)) == len(stack):
            return i+1
        else:
            stack.pop(0)

print(get_marker())
print(get_marker(False))