
import re
with open('input', 'r') as f:
    instructions = f.read().splitlines()
    
direction = {
    'R' : (0,1),
    'L' : (0, -1),
    'U' : (-1, 0),
    'D' : (1, 0),
}
def adj(fr, to):
    return abs(to[1]-fr[1]) <= 1 and abs(to[0]-fr[0]) <= 1

snake = [[0,0] for _ in range(10)]
neck = {(0,0)}
tail = {(0,0)}
for instruction in instructions:
    d, dist = instruction.split()
    dist = int(dist)
    for i in range(dist):
        dy, dx = direction[d]
        head = snake[0]
        head[0] += dy
        head[1] += dx
        for h,t in zip(snake, snake[1:]):
            if adj(h, t):
                continue
            for i in range(2):
                if abs(h[i]-t[i]) < 2:
                    t[i] = h[i]
                else:
                    t[i] += 1 if h[i] > t[i] else -1
        neck.add(tuple(snake[1]))
        tail.add(tuple(snake[-1]))
print(len(neck))
print(len(tail))