import re
from itertools import combinations

with open('input', 'r') as f:
    lines = f.read().splitlines()
best_max = 0
best_rate = 0


class Node:
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate

    def __repr__(self):
        return f'{self.name} - {self.rate}'

    def __gt__(self, other):
        return True


nodes = {}
dist = {}
nodes_with_rates = []
for line in lines:
    name, *tos = re.findall('[A-Z]{2}', line)
    flow_rate = int(re.search('\d+', line)[0])
    nodes[name] = Node(name, flow_rate)
    if flow_rate:
        nodes_with_rates.append(nodes[name])

    for to in tos:
        dist[(name, to)] = 1
        dist[(to, name)] = 1


for intermediate_node in nodes:
    for fr in nodes:
        for to in nodes:
            if fr == to:
                dist[(fr, to)] = 1
                continue
            new = dist.get((fr, intermediate_node), float('inf')) + \
                dist.get((intermediate_node, to), float('inf'))
            dist[(fr, to)] = min(new, dist.get((fr, to), float('inf')))


def DFS(results, visited=[nodes['AA']], to_visit=set(nodes_with_rates), volume=0, time=0):
    if time >= 30:
        results.append((volume, set(visited)))
        return
    rate = sum([node.rate for node in visited])
    for node in to_visit:
        time_spent = dist[(visited[-1].name, node.name)] + 1
        # +1 for turning on valve
        if time + time_spent >= 30:
            time_spent = 30 - time
        DFS(results, visited + [node], to_visit -
            {node}, volume + rate*time_spent, time + time_spent)
    if not to_visit:
        DFS(results, visited, to_visit, volume + rate * (30-time), 30)


results = []
DFS(results, time=0)
print(max(results))

results = []
DFS(results, time=4)
best_v = 0
for (v1, x), (v2, y) in combinations(reversed(sorted(results)), 2):
    if v1 + v2 < best_v:
        break
    if len(x & y) == 1:
        if (new_v := v1 + v2) > best_v:
            best_v = new_v
            best_paths = (x, y)

print(best_v, best_paths)
