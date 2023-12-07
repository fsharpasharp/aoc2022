from collections import defaultdict
scores = defaultdict(int) | {(0, 0): 4, (1, 1): 5, (2, 2): 6, (0, 1): 8, (1, 2): 9, (2, 0): 7, (0, 2): 3, (1, 0): 1, (2, 1): 2}
whatToPlay = {(0, 1): 0, (0, 2): 1, (0, 0): 2, (1, 0): 0, (1, 1): 1, (1, 2): 2, (2, 2): 0, (2, 0): 1, (2, 1): 2}

with open('input', 'r') as f:
    chars = f.read().split()

scoreWrong = 0
scoreCorrect = 0
for x, y in zip(chars[::2], chars[1::2]):
    scoreWrong += scores[ord(x)-ord('A'), ord(y)-ord('X')]

    left = ord(x)-ord('A')

    play = whatToPlay[left, ord(y)-ord('X')]
    scoreCorrect += scores[left, play]
print(scoreWrong)
print(scoreCorrect)
