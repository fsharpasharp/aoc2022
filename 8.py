from itertools import repeat
with open('miniinput', 'r') as f:
    heights = f.read().splitlines()

rows = len(heights)
columns = len(heights[0])


def rows_and_cols(rows, cols):
    x = []
    for i in range(rows):
        t = list(zip(repeat(i), range(cols)))
        x.append(t)
        x.append(t[::-1])
    for i in range(cols):
        t = list(zip(range(rows), repeat(i)))
        x.append(t)
        x.append(t[::-1])
    return x


visible = [[False for j in range(columns)] for i in range(rows)]
for sequence in rows_and_cols(columns, rows):
    minimum = -1
    for i,j in sequence:
        print(i,j)
        if (height := int(heights[i][j])) > minimum: 
            minimum = height
            visible[i][j] = True

    
def calc_score(y, x):
    height = int(heights[y][x])
    up = 0
    for i in range(y+1, rows):
        up += 1
        if int(heights[i][x]) >= height:
            break

    down = 0
    for i in range(y-1, -1, -1):
            down += 1
            if int(heights[i][x]) >= height:
                break

    right = 0
    for j in range(x+1, columns):
            right += 1
            if int(heights[y][j]) >= height:
                break

    left = 0
    for j in range(x-1, -1, -1):
            left += 1
            if int(heights[y][j]) >= height:
                break

    return up*down*left*right

score = [[0 for j in range(columns)] for i in range(rows)]
for y in range(rows):
    for x in range(columns):
        score[y][x] = calc_score(y,x)

print(max([max(s) for s in score]))
print(sum([sum(row) for row in visible]))