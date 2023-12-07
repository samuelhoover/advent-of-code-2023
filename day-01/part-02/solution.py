import re


sum = 0
num_dict = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

with open('../input.txt', mode='r') as f:
    for line in f:
        results = re.findall(
            r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))',
            line
        )

        if results[0] in num_dict:
            first_num = num_dict[results[0]]
        else:
            first_num = results[0]

        if results[-1] in num_dict:
            last_num = num_dict[results[-1]]
        else:
            last_num = results[-1]

        sum += int(first_num + last_num)

print(sum)
