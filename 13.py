from functools import cmp_to_key
with open('input', 'r') as f:
    pars = f.read().split('\n\n')

def compare(a, b):
    match a, b:
        case int(), int():
            if a == b:
                return 0
            return -1 if a < b else 1
        case int(), list():
            return compare([a],b)
        case list(), int():
            return compare(a,[b])
        case list(), list():
            for x, y in zip(a, b):
                if (v := compare(x, y)) != 0:
                    return v
            if len(a) == len(b):
                return 0
            return -1 if len(a) < len(b) else 1

s = 0
div1 = [[2]]
div2 = [[6]]
l = [div1, div2]
for i, par in enumerate(pars):
    left, right = map(eval, par.splitlines())
    l.append(left)
    l.append(right)
    if compare(left, right) == -1:
        s += i+1

print(s)
ss = sorted(l, key=cmp_to_key(compare))
print((ss.index(div1)+1) * (ss.index(div2)+1))