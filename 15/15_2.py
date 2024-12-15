with open('15/example.txt', 'r') as f:
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
boxes = []
walls = []
h = len(warehouse)
w = len(warehouse[0])

# find robot and boxes
for i in range(h):
    for j in range(w):
        if warehouse[i][j] == '@':
            robot = [i, j]
        elif warehouse[i][j] == '[':
            boxes.append([i, j])
        elif warehouse[i][j] == '#':
            walls.append([i, j])


def draw_map():
    wh = []
    for _ in range(h):
        line = []
        for __ in range(w):
            line.append('.')
        wh.append(line)
    wh[robot[0]][robot[1]] = '@'
    for wall in walls:
        wh[wall[0]][wall[1]] = '#'
    for b in boxes:
        wh[b[0]][b[1]] = '['
        wh[b[0]][b[1] + 1] = ']'
    return wh


def move_boxes(i, j, d):
    if d in '<>':
        while warehouse[i][j] != '#' and warehouse[i][j] != '.':
            j += dirs[d][1]
        if warehouse[i][j] == '#':
            return
        temp_target_boxes = [k for k, x in enumerate(boxes) if x[0] == i]
        target_boxes = []
        for b in temp_target_boxes:
            pass
        for k in target_boxes:
            boxes[k][1] += dirs[d][1]
        robot[1] += dirs[d][1]
        return
    else:
        pass


    


    
# move robot
for m in movements:
    i, j = robot[0], robot[1]
    next_i, next_j = i + dirs[m][0], j + dirs[m][1]
    if warehouse[next_i][next_j] == '.':
        robot = [next_i, next_j]
        warehouse = draw_map()
    elif warehouse[next_i][next_j] == '#':
        continue
    elif warehouse[next_i][next_j] in '[]':
        move_boxes(i, j, m)
        warehouse = draw_map()

# calculate result
result = 0
for i in range(len(warehouse)):
    for j in range(len(warehouse[i])):
        if warehouse[i][j] == '[':
            result += 100 * i + j


print(result)
