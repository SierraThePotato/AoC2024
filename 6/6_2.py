with open('6/input.txt', 'r') as f:
    input_str = f.read()

result = 0

facing = {
    '^': ((-1, 0), '>'),
    '>': ((0, 1), 'v'),
    'v': ((1, 0), '<'),
    '<': ((0, -1), '^')
}

guard_map = [[y for y in x] for x in input_str.split('\n')]
position = [0, 0] # x and y coordinates
direction = ''

# find starting position
for i in range(len(guard_map)):
    for j in range(len(guard_map[i])):
        if guard_map[i][j] in facing.keys():
            position[0] = i
            position[1] = j
            direction = guard_map[i][j]
            break


def new_obstacle(row, col):
    temp_map = [row[:] for row in guard_map]
    temp_map[row][col] = '#'
    temp_pos = position[:]
    temp_dir = direction
    visited = set()

    while True: 
        state = (temp_pos[0], temp_pos[1], temp_dir)
        if state in visited:
            return True
        visited.add(state)

        temp_next_pos = [temp_pos[0] + facing[temp_dir][0][0], temp_pos[1] + facing[temp_dir][0][1]]
        if temp_next_pos[0] < len(temp_map) and temp_next_pos[1] < len(temp_map[0]) and temp_next_pos[0] >= 0 and temp_next_pos[1] >= 0:
            if temp_map[temp_next_pos[0]][temp_next_pos[1]] == '#':
                temp_dir = facing[temp_dir][1]
            else:
                temp_pos = temp_next_pos
        else:
            return False


for i in range(len(guard_map)):
    for j in range(len(guard_map[i])):
        if guard_map[i][j] == '.' and [i, j] != position:
            if new_obstacle(i, j):
                result += 1

print(result)
