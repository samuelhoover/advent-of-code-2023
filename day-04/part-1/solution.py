with open('../input.txt', mode='r') as f:
    data = [line.split(':')[1] for line in f]

game_dict = {}
game_dict['win'] = [line.split('|')[0].strip().split() for line in data]
game_dict['play'] = [line.split('|')[1].strip().split() for line in data]

totalsum = 0
W, P = game_dict.values()
for (w, p) in zip(W, P):
    numsum = [1 for _p in p if _p in w]
    if len(numsum) > 0:
        totalsum += (2 ** (len(numsum) - 1))

print(totalsum)
