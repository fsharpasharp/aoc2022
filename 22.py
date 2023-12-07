import re
import os

with open('mini', 'r') as f:
    m, instructions = f.read().split('\n\n')

lines = m.splitlines()
rows = len(lines)
cols = len(lines[0])
for i, line in enumerate(lines):
    lines[i] = line.ljust(cols, ' ')


one_third = cols//3
left = []
middle = []
right = []
xs = [left, middle, right]
for line in lines:
    for i, x in enumerate(xs):
        x.append(line[one_third*i:one_third*(i+1)])


A = middle[:50]
B = right[:50]
C = middle[50:100]
D = middle[100:150]
E = left[100:150]
F = left[150:200]

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3


n = {
    0: 'RIGHT',
    1: 'DOWN',
    2: 'LEFT',
    3: 'UP',
}


class Tile:
    def __init__(self, m, name):
        self.m = m[:]
        self.c = {}
        self.name = name

    def __repr__(self):
        return f'{self.name} connected in {[n[x] for x in self.c.keys()]}'

    def connect(self, t, d, orientation):
        self.c[d] = (t, orientation)


A, B, C, D, E, F = Tile(A, 'A'), Tile(B, 'B'), Tile(
    C, 'C'), Tile(D, 'D'), Tile(E, 'E'), Tile(F, 'F')

A.connect(B, RIGHT, 0)
A.connect(C, DOWN, 0)
A.connect(F, UP, 3)
A.connect(D, LEFT, 2)
B.connect(A, LEFT, 0)
B.connect(F, UP, 0)
B.connect(E, RIGHT, 2)
B.connect(C, DOWN, 3)
C.connect(A, UP, 0)
C.connect(B, RIGHT, 1)
C.connect(D, LEFT, 1)
C.connect(E, DOWN, 0)
D.connect(A, LEFT, RIGHT)
D.connect(C, UP, RIGHT)
D.connect(E, RIGHT, RIGHT)
D.connect(F, DOWN, DOWN)
E.connect(C, UP, 0)
E.connect(B, RIGHT, 2)
E.connect(D, LEFT, 0)
E.connect(F, DOWN, 3)
F.connect(D, UP, 0)
F.connect(B, DOWN, 0)
F.connect(A, LEFT, 1)
F.connect(E, RIGHT, 1)


parsed_instructions = []
while instructions:
    m = re.search('^\d+', instructions)
    if m:
        instructions = instructions[m.end():]
        parsed_instructions.append(int(m[0]))
    else:
        parsed_instructions.append(instructions[0])
        instructions = instructions[1:]

y, x = 0, 0
board = D
orientation = 0

move = {
    RIGHT: lambda y, x: (y, x+1),
    UP: lambda y, x: (y-1, x),
    LEFT: lambda y, x: (y, x-1),
    DOWN: lambda y, x: (y+1, x),
}

sz = 50
for inst in parsed_instructions:
    if type(inst) == int:
        while inst > 0:
            prev_x = x
            prev_y = y
            prev_board = board
            prev_orientation = orientation
            y, x = move[orientation](y, x)

            new_facing = 0

            if x == -1:
                board, new_facing = board.c[LEFT]
            elif x == sz:
                board, new_facing = board.c[RIGHT]
            elif y == -1:
                board, new_facing = board.c[UP]
            elif y == sz:
                board, new_facing = board.c[DOWN]

            x = (x + 50) % 50
            y = (y + 50) % 50

            if new_facing == 0:
                y = 50 - y
                y, x = x,y
            if new_facing == 1:
                y = 50 - y
                y, x = x,y
            if new_facing == 2:
                y = 50 - y
                y, x = x,y
            elif new_facing == 3:
                y = 50 - y
                y, x = x,y

            orientation = new_facing

            if board.m[y][x] == '#':
                x = prev_x
                y = prev_y
                board = prev_board
                orientation = prev_orientation

                os.system('clear')
                for i in range(50):
                    for j in range(50):
                        if (i, j) == (y, x):
                            print('E', end='')
                        else:
                            print(board.m[i][j], end='')
                    print()
                print(orientation)
                print(y, x)
                print(new_facing, board.name, inst)
                input()
                break
            
            os.system('clear')
            for i in range(50):
                for j in range(50):
                    if (i, j) == (y, x):
                        print('E', end='')
                    else:
                        print(board.m[i][j], end='')
                print()
            print(orientation)
            print(y, x)
            print(new_facing, board.name, inst)
            input()

            inst -= 1

    elif inst == 'R':
        orientation += 1
    elif inst == 'L':
        orientation -= 1

    orientation = (orientation + 4) % 4

    os.system('clear')
    for i in range(50):
        for j in range(50):
            if (i, j) == (y, x):
                print('E', end='')
            else:
                print(board.m[i][j], end='')
        print()
    print(orientation)
    print(y, x)
    print(new_facing, board.name, inst)
    input()


print(board)
print(y+1, x+1, orientation)

# The final password is the sum of 1000 times the row, 4 times the column, and the facing.
