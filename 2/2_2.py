
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


def is_removed_safe(levels):
    for i in range(len(levels)):
        rem_list = levels[:i] + levels[i + 1:]
        if is_safe(rem_list):
            return True
    return False


for line in input_str.strip().split('\n'):
    levels = [int(i) for i in line.strip().split(' ')]
    if is_safe(levels):
        safe_ctr += 1
    elif is_removed_safe(levels):
        safe_ctr += 1
        

print(safe_ctr)
