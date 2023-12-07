sum = 0

with open('../input.txt', mode='r') as f:
    for line in f:
        for c in line:  # forward search
            if c.isnumeric():
                first_num = c
                break
        for c in line[::-1]:  # reverse search
            if c.isnumeric():
                last_num = c
                break
        sum += int(first_num + last_num)

print(sum)
