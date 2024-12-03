import re
with open('3/input.txt', 'r') as f:
    input_str = f.read().replace('\n', ' ')

result = 0


def count_matches(p):
    r = 0
    matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)', p.strip())
    for match in matches:
        nums = match.split('(')[1].strip(')').split(',')
        r += int(nums[0]) * int(nums[1])
    return r


parts = input_str.split('don\'t()')

result += count_matches(parts[0]) # you count the start

parts_str = [part.split('do()') for part in parts]

for i in range(1, len(parts_str)): # the first is already counted
    for j in range(1, len(parts_str[i])): # the first of each row is right after the don't, the rest are dos
        result += count_matches(parts_str[i][j])


print(result)