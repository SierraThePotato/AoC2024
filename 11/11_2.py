from functools import cache
with open('11/input.txt', 'r') as f:
    input_str = f.read().strip()


stones = input_str.split(' ')

@cache
def process_stone(stone, i):
    if i == 0:
        return 1
    else:
        if stone == '0':
            return process_stone('1', i - 1)
        elif len(stone) % 2 == 0:
            half = int(len(stone)/2)
            return process_stone(stone[:half], i - 1) + process_stone(stone[half:-1].lstrip('0') + stone[-1], i - 1)
        else:
            return process_stone(str(int(stone) * 2024), i - 1)


result = 0
for stone in stones:
    result += process_stone(stone, 75)


print(result)
