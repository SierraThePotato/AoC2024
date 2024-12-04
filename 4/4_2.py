import re
with open('4/input.txt', 'r') as f:
    input_str = f.read().split('\n')

result = 0
valid = ['M', 'S']

for i in range(len(input_str)):
    for j in range(len(input_str[i])):
        if input_str[i][j] == 'A':
            corner = ''
            if i > 0 and j > 0:
                if input_str[i-1][j-1] in valid:
                    corner = input_str[i-1][j-1]
                else:
                    continue
            else:
                continue
            if i < len(input_str) - 1 and j < len(input_str[i]) - 1: 
                if input_str[i+1][j+1] in valid:
                    if corner == 'M' and input_str[i+1][j+1] == 'S' or corner == 'S' and input_str[i+1][j+1] == 'M':
                        pass
                    else:
                        continue
                else:
                    continue
            else:
                continue
            if i > 0 and j < len(input_str[i]) - 1:
                if input_str[i-1][j+1] in valid:
                    corner = input_str[i-1][j+1]
                else:
                    continue
            else:
                continue
            if i < len(input_str) - 1 and j > 0: 
                if input_str[i+1][j-1] in valid:
                    if corner == 'M' and input_str[i+1][j-1] == 'S' or corner == 'S' and input_str[i+1][j-1] == 'M':
                        pass
                    else:
                        continue
                else:
                    continue
            else:
                continue
            result += 1



print(result)
