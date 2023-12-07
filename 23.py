from collections import defaultdict
with open('mini', 'r') as f:
    lines = f.read().splitlines()

pos = {x-y*1j for y, line in enumerate(lines)
       for x, c in enumerate(line) if c == '#'}

rule_one = {-1+1j, 1j, 1 + 1j}
rule_two = {-x for x in rule_one}
rule_three = {x*1j for x in rule_one}
rule_four = {-x for x in rule_three}
adjacent = rule_one | rule_two | rule_three | rule_four
rules = [(rule_one, 1j), (rule_two, -1j), (rule_three, -1), (rule_four, +1)]


def add(pos, moves): return {pos + move for move in moves}


i = 1
eneho = True
while eneho == eneho:
    candidates = defaultdict(int)
    next_move = {}
    for e in pos:
        if not add(e, adjacent) & pos:
            continue
        for (rule, move) in rules:
            if not add(e, rule) & pos:
                candidates[e+move] += 1
                next_move[e] = e+move
                break

    new_pos = set()
    for e in pos:
        if e not in next_move:
            new_pos.add(e)
            continue

        c = next_move[e]
        if candidates[c] != 1:
            new_pos.add(e)
            continue

        new_pos.add(c)

    rules.append(rules[0])
    rules = rules[1:]
    if pos == new_pos:
        break
    pos = new_pos
    if i == 10:
        min_x, min_y = [float('inf')]*2
        max_x, max_y = [float('-inf')]*2
        for e in pos:
            min_x = min(e.real, min_x)
            max_x = max(e.real, max_x)

            min_y = min(e.imag, min_y)
            max_y = max(e.imag, max_y)

        x = (max_x-min_x)+1
        y = (max_y-min_y)+1

        print(x*y - len(pos))
    i += 1

print(i)
