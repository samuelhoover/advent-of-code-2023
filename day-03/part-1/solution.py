import re


with open('../input.txt', mode='r') as f:
    data = [line.strip() for line in f]

symbols = {
    (i, j): []
    for i, line in enumerate(data)
    for j, sym in enumerate(line)
    if sym not in '0123456789.'
}

for i, line in enumerate(data):
    for n in re.finditer(r'\d+', line):
        edges = {
            (i, j) for i in (i - 1, i, i + 1)
            for j in range(n.start() - 1, n.end() + 1)
        }

        for idx in edges & symbols.keys():
            symbols[idx].append(int(n.group()))

print(sum(sum(p) for p in symbols.values()))
