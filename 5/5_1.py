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


for update in updates:
    if is_correct(update, ordering):
        result += int(update[int(len(update)/2)])



print(result)
