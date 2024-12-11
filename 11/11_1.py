with open('11/input.txt', 'r') as f:
    input_str = f.read().strip()


stones = input_str.split(' ')

for _ in range(25):
    new_stones = []
    for stone in stones:
        if stone == '0':
            new_stones.append('1')
        elif len(stone) % 2 == 0:
            half = int(len(stone)/2)
            new_stones.append(stone[:half])
            new_s = stone[half:].lstrip('0')
            if new_s == '':
                new_stones.append('0')
            else:
                new_stones.append(new_s)
        else:
            new_stones.append(str(int(stone) * 2024))
    stones = new_stones

print(len(stones))
