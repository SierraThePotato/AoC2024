with open('15/input.txt', 'r') as f:
    input_str = f.read().strip()

warehouse = [[y for y in x] for x in input_str.split('\n\n')[0].split('\n')]
movements = input_str.split('\n\n')[1].replace('\n', '')

dirs = {
    '>': (0, 1),
    '<': (0, -1),
    '^': (-1, 0),
    'v': (1, 0)
}

robot = [0, 0]

# find robot
for i in range(len(warehouse)):
    if robot != [0, 0]:
        break
    for j in range(len(warehouse[i])):
        if warehouse[i][j] == '@':
            robot = [i, j]
            break


def is_movable(i, j, d):
    while 0 < i < len(warehouse) - 1 and 0 < j < len(warehouse[0]) - 1:
        if warehouse[i][j] == '.':
            return True
        i, j = i + dirs[d][0], j + dirs[d][1]
        if warehouse[i][j] == '#':
            break
    return False


def move_boxes(i, j, d):
    while warehouse[i][j] != '.':
        i, j = i + dirs[d][0], j + dirs[d][1]
    while warehouse[i][j] != '@':
        warehouse[i][j] = 'O'
        i, j = i - dirs[d][0], j - dirs[d][1]
        next_i, next_j = i - dirs[d][0], j - dirs[d][1]
        if warehouse[next_i][next_j] == '@':
            warehouse[i][j] = '@'
            warehouse[next_i][next_j] = '.'
            return [i, j]


# move robot
for m in movements:
    i, j = robot[0], robot[1]
    next_i, next_j = i + dirs[m][0], j + dirs[m][1]
    if next_i < 1 or next_i >= len(warehouse) - 1 or next_j < 1 or next_j >= len(warehouse[0]) - 1:
        continue
    if warehouse[next_i][next_j] == '.':
        robot = [next_i, next_j]
        warehouse[next_i][next_j] = '@'
        warehouse[i][j] = '.'
    elif warehouse[next_i][next_j] == '#':
        continue
    elif warehouse[next_i][next_j] == 'O':
        if is_movable(next_i, next_j, m):
            robot = move_boxes(next_i, next_j, m)
        else:
            continue


# calculate result
result = 0
for i in range(len(warehouse)):
    for j in range(len(warehouse[i])):
        if warehouse[i][j] == 'O':
            result += 100 * i + j


print(result)
