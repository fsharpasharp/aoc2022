score = lambda c : ord(c)-ord('A')+27 if c.isupper() else ord(c)-ord('a')+1

with open('input', 'r') as f:
  lines = f.read().split()

s = 0
for line in lines:
  half = len(line)//2
  s += score((set(line[:half]) & set(line[half:])).pop())
print(s)

s = 0
lines = [set(x) for x in lines]
for i in range(0, len(lines), 3):
  s += score((lines[i] & lines[i+1] & lines[i+2]).pop())
print(s)
