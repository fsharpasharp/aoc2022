from collections import deque, defaultdict

with open('input', 'r') as f:
    lines = f.read().splitlines()

blizzards = defaultdict(set)

for y, line in enumerate(lines[1:-1]):
    for x, char in enumerate(line[1:-1]):
        if char != '.':
            blizzards[char].add((x+y*1j))

c = {'>': 1, '<': -1, '^': -1j, 'v': 1j}

rows = len(lines) - 2
cols = len(lines[0]) - 2


def in_blizzard(pos, time):
    for k, v in c.items():
        p = pos - time * v
        p = (p.real + cols) % cols + ((p.imag + rows) % rows) * 1j
        if p in blizzards[k]:
            return True
    return False


deq = deque([(-1j, 0, 0)])
seen = set()

stage = 0
printOnce = True
while deq:
    pos, time, stage = deq.popleft()
    if pos == (cols-1) + rows*1j:
        if printOnce:
            print(f'End found after {time}')
            printOnce = False
        if stage == 2:
            print(f'End found after {time}')
            exit()
        stage = 1
    time += 1
    if stage and pos == -1j:
        stage = 2

    for move in list(c.values()) + [0]:
        new_pos = pos+move
        if (new_pos, time, stage) in seen: continue
        seen.add((new_pos, time, stage))
        if new_pos == -1j or new_pos == (cols-1) + rows*1j: pass
        elif in_blizzard(new_pos, time): continue
        elif not 0 <= new_pos.imag < rows: continue
        elif not 0 <= new_pos.real < cols: continue
        deq.append((new_pos, time, stage))
