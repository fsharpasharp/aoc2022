from collections import deque
with open('input', 'r') as f:
    lines = f.read().splitlines()
    
def find(lines, char):
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == char:
                return i,j

cols = len(lines[0])
rows = len(lines)
directions = [(1,0), (-1,0), (0, 1), (0,-1)]

q = deque([(*find(lines, 'E'), ord('E'), 0)])

m = {
    ord('E'): ord('z'),
    ord('S'): ord('a'),
}
visited = set()
while q:
    y, x, val, steps = q.popleft()
    if (y, x, val) in visited:
        continue
    visited.add((y,x, val))
    if not (0 <= y < rows) or not (0 <= x < cols):
        continue
    curVal = ord(lines[y][x])
    curVal = m.get(curVal, curVal)
    if curVal-val < -1:
        continue
    if curVal == ord('a'):
        print(steps)
        break
    for i,j in directions:
        q.append((y+i, x+j, curVal, steps+1))