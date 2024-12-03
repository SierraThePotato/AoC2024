import re
with open('3/input.txt', 'r') as f:
    input_str = f.read().replace('\n', ' ')

result = 0

matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)', input_str.strip())

for match in matches:
    nums = match.split('(')[1].strip(')').split(',')
    result += int(nums[0]) * int(nums[1])


print(result)
