import numpy as np

nums = [n.rstrip('\n') for n in open("01_input.txt")]
x = []
aux = []
for n in nums:
    if n != '':
        aux.append(n)
    else:
        x.append(aux)
        aux = []

print(x)

aux, elfs = 0, []
for n in nums:
    if n != '':
        aux += int(n)
    else:
        elfs.append(aux)
        aux = 0

ind = np.argmax(elfs)
max = elfs[ind]
print(max)

for i in range(2):
    elfs.pop(ind)
    ind = np.argmax(elfs)
    max += elfs[ind]

print(max)