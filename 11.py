import re

class Monkey():
    def __init__(self, starting_items, eval_expr, divisible_by, true_monkey, false_monkey):
        self.starting_items = starting_items
        self.eval_expr = eval_expr
        self.divisible_by = divisible_by
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.items_inspected = 0

    def __str__(self):
        return f'{self.starting_items} {self.eval_expr} {self.divisible_by}'

    def update_references(self, monkeys):
        self.true_monkey = monkeys[self.true_monkey]
        self.false_monkey = monkeys[self.false_monkey]
        prod = 1
        for factor in [monkey.divisible_by for monkey in monkeys]:
            prod *= factor
        self.N = prod


    def add(self, item):
        self.starting_items.append(item)

    def turn(self):
        while self.starting_items:
            old = self.starting_items.pop()
            self.items_inspected += 1
            # old %= self.N
            new = eval(self.eval_expr)
            if new % self.divisible_by == 0:
                self.true_monkey.add(new)
            else:
                self.false_monkey.add(new)

def parse(string):
    lines = string.splitlines()
    starting_items = list(map(int, re.findall('\d+', lines[1])))
    eval_expr = lines[2][19:]
    divisible_by = int(re.search('\d+',lines[3])[0])
    true_monkey = int(re.search('\d+', lines[4])[0])
    false_monkey = int(re.search('\d+', lines[5])[0])
    return Monkey(starting_items, eval_expr, divisible_by, true_monkey, false_monkey)

with open('input', 'r') as f:
    instructions = f.read().split('\n\n')

monkeys = list(map(parse, instructions))
for monkey in monkeys:
    monkey.update_references(monkeys)

for i in range(100):
    for monkey in monkeys:
        monkey.turn()
m1, m2, = sorted(map(lambda x : x.items_inspected, monkeys))[-2:]
print(m1*m2)
