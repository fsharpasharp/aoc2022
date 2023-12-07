from itertools import cycle
cols = 7


def flat(cave, x, y):
    if x < 0:
        return False
    if x + 3 >= cols:
        return False

    for i in range(4):
        if (x+i, y) in cave:
            return False
    return True


def flat_place(cave, x, y):
    cave |= {(x+i, y) for i in range(4)}
    return y


def plus(cave, x, y):
    if x < 0:
        return False
    if x + 2 >= cols:
        return False

    if (x, y+1) in cave:
        return False
    for i in range(3):
        if (x+1, y+i) in cave:
            return False
    if (x+2, y+1) in cave:
        return False
    return True


def plus_place(cave, x, y):
    cave.add((x, y+1))
    cave |= {(x+1, y+i) for i in range(3)}
    cave.add((x+2, y+1))
    return y+2


def reverse_l(cave, x, y):
    if x < 0:
        return False
    if x + 2 >= cols:
        return False

    if (x, y) in cave:
        return False
    if (x+1, y) in cave:
        return False
    for i in range(3):
        if (x+2, y+i) in cave:
            return False
    return True


def reverse_l_place(cave, x, y):
    cave.add((x, y))
    cave.add((x+1, y))
    cave |= {(x+2, y+i) for i in range(3)}
    return y+2


def eye(cave, x, y):
    if x < 0:
        return False
    if x >= cols:
        return False

    for i in range(4):
        if (x, y+i) in cave:
            return False

    return True


def place_eye(cave, x, y):
    cave |= {(x, y+i) for i in range(4)}
    return y+3


def box(cave, x, y):
    if x < 0:
        return False
    if x + 1 >= cols:
        return False

    if (x, y) in cave:
        return False
    if (x, y+1) in cave:
        return False
    if (x+1, y) in cave:
        return False
    if (x+1, y+1) in cave:
        return False
    return True


def place_box(cave, x, y):
    cave.add((x, y))
    cave.add((x, y+1))
    cave.add((x+1, y))
    cave.add((x+1, y+1))
    return y+1


with open('mini', 'r') as f:
    instructions = f.read().strip()


pieces = [(flat, flat_place), (plus, plus_place), (reverse_l,
                                                   reverse_l_place), (eye, place_eye), (box, place_box)]

cave = {(i, 0) for i in range(7)}
i = 0
floor = 0

millionth_floor = 0
heights = []
seen = {}
remainder = 0
for dropped, (placable, place) in enumerate(cycle(pieces)):
    if dropped == 1_000_000_000_000:
        break
    # if dropped == 639258+452:
    #     print(floor)
    #     input()
    # if floor > 1_000_000:
    #     o = set()
    #     st = ""
    #     for j in range(floor, floor-100, -1):
    #         for eks in range(0, 7):
    #             if (eks, j) in cave:
    #                 st += "#"
    #             else:
    #                 st += '.'
    #         st += '\n'
    #     state = (st, dropped % 5, i)
    #     if state in seen:
    #         print(seen[state])
    #         old_dropped, old_floor = seen[state]

    #         print(
    #             f'delta x: {dropped-old_dropped}\ndelta y: {floor-old_floor}')
    #         input()
    #     seen[state] = (dropped, floor)
    if dropped % (637543+452) == 0:
        print(dropped, floor)
        input()
    y = floor + 4
    # print(y)
    # input()
    x = 2
    while placable(cave, x, y):
        inst = instructions[i]
        # print(instructions[i])
        i = (i+1) % len(instructions)
        old_x = x
        if inst == '>':
            x += 1
        else:
            x -= 1
        if not placable(cave, x, y):
            x = old_x
        y -= 1
        # print(x)

    y += 1
    # print(i)
    floor = max(place(cave, x, y), floor)
    heights.append(floor)

    # for j in range(100, floor-8, -1):
    #     for eks in range(0, 7):
    #         if (eks, j) in cave:
    #             print('#', end='')
    #         else:
    #             print('.', end='')
    #     print()

    # input()

print(floor)
