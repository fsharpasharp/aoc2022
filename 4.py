import re

with open('input', 'r') as f:
  x = [int(x) for x in re.findall('\d+', f.read())]

s0 = 0 
s1 = 0
for i in range(0, len(x), 4):
  l, r, d, u = x[i], x[i+1], x[i+2], x[i+3]
  b lamba a,b,c,d : a <= b <= d and a <= c <= d
  s0 += b(l,d,r) and b(l,r,u) l <= d and u <= r or d <= l and r <= u
  s1 += \
    l <= d <= r or \
    l <= u <= r or \
    d <= l <= u or \
    d <= r <= u
print(s0)
print(s1)