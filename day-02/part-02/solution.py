import re


numsum = 0

with open('../input.txt', mode='r') as f:
    for line in f:
        game_line, sets_line = line.split(':')

        pull = {'r': 0, 'g': 0, 'b': 0}

        for num, col in re.findall(r'(\d+) (\w)', sets_line):
            pull[col] = max(pull[col], int(num))

        numsum += (pull['r'] * pull['g'] * pull['b'])

print(numsum)
