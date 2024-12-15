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


# expand map
new_warehouse = [[] for _ in range(len(warehouse))] 
for i in range(len(warehouse)):
    for t in warehouse[i]:
        if t == '@':
            new_warehouse[i].append('@')
            new_warehouse[i].append('.')
        elif t == 'O':
            new_warehouse[i].append('[')
            new_warehouse[i].append(']')
        else:
            new_warehouse[i].append(t)
            new_warehouse[i].append(t)
            
warehouse = new_warehouse

robot = [0, 0]


# find robot
for i in range(len(warehouse)):
    if robot != [0, 0]:
        break
    for j in range(len(warehouse[i])):
        if warehouse[i][j] == '@':
            robot = [i, j]
            break


def check_vertical(i, j, d):
    if warehouse[i][j] == '[':
        bli, blj = i, j
        bri, brj = i, j + 1
    else:
        bli, blj = i, j - 1
        bri, brj = i, j
    left = warehouse[bli + d][blj]
    right = warehouse[bri + d][brj]
    if left == '#' or right == '#':
        return False
    if left == '.' and right == '.':
        return True
    if left == '[':
        if check_vertical(bli + d, blj, d):
            return True
    lc = left == '.'
    rc = right == '.'
    if not lc:
        lc = check_vertical(bli + d, blj, d)
    if not rc:
        rc = check_vertical(bri + d, brj, d)
    return lc and rc


def move_vertical(i, j, d):
    if warehouse[i][j] == '[':
        bli, blj = i, j
        bri, brj = i, j + 1
    else:
        bli, blj = i, j - 1
        bri, brj = i, j
    left = warehouse[bli + d][blj]
    right = warehouse[bri + d][brj]
    if left == '[':
        move_vertical(bli + d, blj, d)
        warehouse[bli + d][blj] = '['
        warehouse[bri + d][brj] = ']'
        warehouse[bli][blj] = '.'
        warehouse[bri][brj] = '.'
        return
    lc = left == '.'
    rc = right == '.'
    if not lc:
        move_vertical(bli + d, blj, d)
    if not rc:
        move_vertical(bri + d, brj, d)
    warehouse[bli + d][blj] = '['
    warehouse[bri + d][brj] = ']'
    warehouse[bli][blj] = '.'
    warehouse[bri][brj] = '.'
    return
    
    
def move_box(i, j, d):
    if d in '<>':
        move = dirs[d][1]
        while warehouse[i][j] != '#' and warehouse[i][j] != '.':
            j += move
        if warehouse[i][j] == '#':
            return False
        while warehouse[i][j - move] != '@':
            warehouse[i][j] = warehouse[i][j - move]
            j -= move
        warehouse[i][j] = '.'
        robot[1] += move
        return True
    else:
        move = dirs[d][0]
        if check_vertical(i, j, move):
            move_vertical(i, j, move)
            return True
        return False
    

# move robot
for m in movements:
    i, j = robot[0], robot[1]
    next_i, next_j = i + dirs[m][0], j + dirs[m][1]
    if warehouse[next_i][next_j] == '.':
        robot = [next_i, next_j]
        warehouse[next_i][next_j] = '@'
        warehouse[i][j] = '.'
    elif warehouse[next_i][next_j] == '#':
        continue
    elif warehouse[next_i][next_j] in '[]':
        if move_box(next_i, next_j, m):
            robot = [next_i, next_j]
            warehouse[next_i][next_j] = '@'
            warehouse[i][j] = '.'


# calculate result
result = 0
for i in range(len(warehouse)):
    for j in range(len(warehouse[i])):
        if warehouse[i][j] == '[':
            result += 100 * i + j


print(result)