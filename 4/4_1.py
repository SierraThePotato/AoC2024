import re
with open('4/input.txt', 'r') as f:
    input_str = f.read().split('\n')

result = 0

def find_in_line(line):
    matches_f = re.findall(r'(XMAS)', line.strip())
    matches_b = re.findall(r'(SAMX)', line.strip())

    return len(matches_b) + len(matches_f)

def count(input_str):
    result = 0
    for line in input_str:
        result += find_in_line(line)
    return result


# horizontally
result += count(input_str)


# vertically
temp_str = []
for i in range(len(input_str[0])):
    line = ''
    for j in range(len(input_str)):
        line += input_str[j][i]
    temp_str.append(line)

result += count(temp_str)


# diagonally 1
temp_str = []
for i in range(len(input_str[0]) - 1, -1, -1):
    line = ''
    j = i
    k = 0
    while j < len(input_str[0]) and k < len(input_str):
        line += input_str[k][j]
        j += 1
        k += 1
    temp_str.append(line)
for i in range(1, len(input_str)):
    line = ''
    j = i
    k = 0
    while j < len(input_str) and k < len(input_str[0]):
        line += input_str[j][k]
        j += 1
        k += 1
    temp_str.append(line)

result += count(temp_str)


# diagonally 2
temp_str = []
for i in range(len(input_str[0])):
    line = ''
    j = i
    k = 0
    while j >= 0 and k < len(input_str):
        line += input_str[k][j]
        j -= 1
        k += 1
    temp_str.append(line)
for i in range(1, len(input_str)):
    line = ''
    j = i
    k = len(input_str[0]) - 1
    while j < len(input_str) and k >= 0:
        line += input_str[j][k]
        j += 1
        k -= 1
    temp_str.append(line)


result += count(temp_str)



print(result)
