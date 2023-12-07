with open('mini', 'r') as f:
    lines = f.read().splitlines()

m = {'-': -1, '=': -2, '0': 0, '1': 1, '2': 2}
summa = 0
for line in lines:
    s = 0
    for c in line:
        s *= 5
        s += m[c]
    summa += s


xs = [-2, -1, 0, 1, 2]
# xs = ['=', '-', '0', '1', '2']
counters = [0]*1_000
counters[0] = 0

x = 0
print(summa)
while (x < summa):
    counters[0] += 1
    for i, counter in enumerate(counters):
        if counter == 3:
            counters[i] = -2
            counters[i+1] += 1
        else:
            break

    s = ''
    for counter in counters:
        if counter == -2:
            s += '='
        elif counter == -1:
            s += '-'
        else:
            s += str(counter)
    print(s[::-1])
    input()

