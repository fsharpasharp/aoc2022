import re
with open('input', 'r') as f:
    instructions = f.read().splitlines()

class Directory():
    def __init__(self, parent):
        self.parent = parent
        self.files = dict()
        self.directories = dict()

    def size(self):
        return sum(self.files.values()) + sum([x.size() for x in self.directories.values()])
    
    def __str__(self):
        s = str(self.files)  + '\n'
        for k, v in self.directories.items():
            s += ' size: ' + str(v.size()) + ' ' + str(k) + str(v) + '\n'
        return s


currentDirectory = Directory(None)
directories = {currentDirectory}
instructions = iter(instructions[1:])
for instruction in instructions:
    if instruction.startswith('$ ls'):
        instruction = next(instructions, None)
        while instruction and not instruction.startswith('$'):
            if instruction.startswith('dir'):
                m = re.search('\w+\s*(\S+)', instruction)
                currentDirectory.directories[m[1]] = Directory(currentDirectory)
                directories.add(currentDirectory.directories[m[1]])
            else:
                m = re.search('(\d+)\s*(\S+)', instruction)
                currentDirectory.files[m[2]] = int(m[1])
            instruction = next(instructions, None)
    if not instruction:
        break
    if instruction.startswith('$ cd ..'):
        currentDirectory = currentDirectory.parent
    elif instruction.startswith('$ cd '):
        m = re.search('\$ cd\s*(\S+)', instruction)
        currentDirectory = currentDirectory.directories[m[1]]
    
sizes = [x.size() for x in directories]
print(sum(filter(lambda x : x < 100000, sizes)))

sort = sorted(sizes)
fsSize = 70000000
unused = fsSize - sort[-1]

print(next(x for x in sort if x >= 30000000 - unused))