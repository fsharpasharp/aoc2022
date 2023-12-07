from collections import deque

with open('mini', 'r') as f:
    lines = f.read().splitlines()


cubes = set()
for line in lines:
    n = tuple(int(x) for x in line.split(','))
    cubes.add(n)


def BFS(current, visited):
    count = 0
    q = deque([current])
    while q:
        current = q.popleft()
        for i in range(3):
            for j in [-1, 1]:
                coord = list(current)
                coord[i] += j
                coord = tuple(coord)
                if coord in cubes:
                    count += 1
                    if not coord in visited:
                        visited.add(coord)
                        q.append(coord)
    return count


def flood_fill(c, visited=set()):
    count = 0
    q = deque([c])
    while q:
        current = q.popleft()
        if current in cubes:
            count += 1
            continue
        if current in visited:
            continue
        for i in range(3):
            if not (-50 < current[i] <= 50):
                break
        else:
            visited.add(current)
            for i in range(3):
                for j in [-1, 1]:
                    coord = list(current)
                    coord[i] += j
                    coord = tuple(coord)
                    q.append(coord)
    return count


visited = set()
sides = 0

outside = flood_fill((25, 25, 25))

while cubes:
    cur = list(cubes)[0]
    visited = {cur}
    covered = BFS(cur, visited)
    sides += len(visited)*6-covered
    print(visited, covered)
    cubes -= visited

print(sides, outside)
