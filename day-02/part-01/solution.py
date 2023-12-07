import re


bag = {
    'r': 12,
    'g': 13,
    'b': 14
}

numsum = 0

with open('../input.txt', mode='r') as f:
    for line in f:
        game_line, sets_line = line.split(':')

        pull = {'r': 0, 'g': 0, 'b': 0}

        for num, col in re.findall(r'(\d+) (\w)', sets_line):
            pull[col] = max(pull[col], int(num))

        check = [1 if pull[k] <= bag[k] else 0 for k in bag.keys()]
        if sum(check) == 3:
            numsum += int(game_line[-2:].strip())

print(numsum)
