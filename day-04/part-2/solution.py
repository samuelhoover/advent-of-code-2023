with open('../input.txt', mode='r') as f:
    data = [line.split(':')[1] for line in f]

game_dict = {}
game_dict['win'] = [line.split('|')[0].strip().split() for line in data]
game_dict['play'] = [line.split('|')[1].strip().split() for line in data]

copies = [1 for _ in data]
W, P = game_dict.values()
for i, (w, p) in enumerate(zip(W, P)):
    matches = [1 for _p in p if _p in w]
    for j, _ in enumerate(matches):
        copies[i + j + 1] += copies[i]

print(sum(copies))
