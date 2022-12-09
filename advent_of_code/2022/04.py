input = [n.rstrip('\n') for n in open("04_input.txt")]

def convert(interval):
    a, b = interval.split('-')
    a, b = int(a), int(b)
    x, arr = '', []

    while a != b:
        x += '|'+str(a)+'|'
        arr.append(a)
        a += 1

    x += '|'+str(a)+'|'
    arr.append(a)
    return (x, arr)

result1, result2 = 0, 0
for i in input:
    a, b = i.split(',')
    a, b = convert(a), convert(b)

    if a[0] in b[0] or b[0] in a[0]:
        result1 += 1
    
    aux = list(set(a[1])&set(b[1]))
    if len(aux) > 0:
        result2 += 1

print(result1)
print(result2)