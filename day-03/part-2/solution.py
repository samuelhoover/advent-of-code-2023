import re


with open('../input.txt', mode='r') as f:
    data = [line.strip() for line in f]

gears = {
    (i, j): []
    for i, line in enumerate(data)
    for j, sym in enumerate(line)
    if sym == '*'
}

for i, line in enumerate(data):
    for n in re.finditer(r'\d+', line):
        edges = {
            (i, j) for i in (i - 1, i, i + 1)
            for j in range(n.start() - 1, n.end() + 1)
        }

        for idx in edges & gears.keys():
            gears[idx].append(int(n.group()))

print(sum([(p[0] * p[1]) for p in gears.values() if len(p) == 2]))
