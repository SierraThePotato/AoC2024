import re
with open('5/input.txt', 'r') as f:
    input_str = f.read()

result = 0

ordering = input_str.split('\n\n')[0].split('\n')
ordering_in = [x.split('|') for x in ordering]

ordering = {}

for rule in ordering_in:
    if rule[0] not in ordering.keys():
        ordering[rule[0]] = []
    ordering[rule[0]].append(rule[1])


updates = input_str.split('\n\n')[1].split('\n')
updates = [x.split(',') for x in updates]


def is_correct(update, ordering):
    for i in range(1, len(update)):
        if update[i] in ordering.keys():
            for page in ordering[update[i]]:
                if page in update[:i]:
                    return False
    return True


def fix_update(update, ordering):
    fixed_update = [x for x in update]
    while not is_correct(fixed_update, ordering):
        for i in range(1, len(fixed_update)):
            if fixed_update[i] in ordering.keys():
                for page in ordering[fixed_update[i]]:
                    if page in fixed_update[:i]:
                        fixed_update[i], fixed_update[fixed_update.index(page)] = fixed_update[fixed_update.index(page)], fixed_update[i]           
    return fixed_update


for update in updates:
    if not is_correct(update, ordering):
        fixed_update = fix_update(update, ordering)
        result += int(fixed_update[int(len(fixed_update)/2)])


print(result)
