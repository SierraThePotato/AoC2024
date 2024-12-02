
with open('2/input.txt', 'r') as f:
    input_str = f.read()

safe_ctr = 0


def is_safe(levels):
    dec = levels[0] > levels[1]
    for i in range(0, len(levels) - 1):
        if (dec and levels[i] < levels[i + 1]) or (not dec and levels[i] > levels[i + 1]):
            return False
        if abs(levels[i] - levels[i + 1]) < 1 or abs(levels[i] - levels[i + 1]) > 3:
            return False
    return True


for line in input_str.strip().split('\n'):
    if is_safe([int(i) for i in line.strip().split(' ')]):
        safe_ctr += 1
        

print(safe_ctr)
