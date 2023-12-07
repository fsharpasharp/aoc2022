with open('input', 'r') as f:
    string = f.read()

print([[i for i in range(size, len(string)) if len(set(string[i-size:i])) == size][0] for size in [4,14]])