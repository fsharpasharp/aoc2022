with open('input', 'r') as f:
    instructions = f.read().splitlines()

cycles = [0]*300
cycles[1] = 1
i = 1
for instruction in instructions:
    i += 1
    if mag := instruction[5:]:
        i += 1
        cycles[i] += int(mag)
for i in range(1,len(cycles)):
    cycles[i] += cycles[i-1]
print(sum([cycles[i]*i for i in range(20, 221, 40)]))
cycle = 1
for i in range(0,6):
    for j in range(0,40):
        print('#' if abs(j - cycles[cycle]) <= 1 else '.', end='')
        cycle += 1
    print()