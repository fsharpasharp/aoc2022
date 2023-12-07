import re
with open('input', 'r') as f:
    start, instructions = f.read().split('\n\n')


start = start.splitlines()
instructions = instructions.splitlines()

def setup_rows(start):
    rows = [[]]
    for x in range(len(start[0])):
        row = []
        for y in range(len(start)):
            if start[y][x] not in '[] ':
                row.append(start[y][x])
        if row:
            rows.append(row[::-1])
    return rows

def one_at_a_time(rows, instructions):
    for instruction in instructions:
        count, who, whom = map(int, re.findall('\d+', instruction))
        for _ in range(count):
            rows[whom].append(rows[who].pop())
    return rows

def multiple_at_a_time(rows, instructions):
    for instruction in instructions:
        count, who, whom = map(int, re.findall('\d+', instruction))
        rows[whom] += rows[who][-count:]
        del rows[who][-count:]
    return rows

print(''.join([x[-1] for x in one_at_a_time(setup_rows(start), instructions)[1:]]))
print(''.join([x[-1] for x in multiple_at_a_time(setup_rows(start), instructions)[1:]]))