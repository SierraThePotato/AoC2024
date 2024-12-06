import re
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
            result += 1
            direction = guard_map[i][j]
            break

# move guard 
while True:
    next_position = [position[0] + facing[direction][0][0], position[1] + facing[direction][0][1]]
    if next_position[0] < len(guard_map) and next_position[1] < len(guard_map[0]) and next_position[0] >= 0 and next_position[1] >= 0:
        if guard_map[next_position[0]][next_position[1]] == '#':
            direction = facing[direction][1]
            guard_map[position[0]][position[1]] = direction
        else:
            if guard_map[next_position[0]][next_position[1]] == '.':
                result += 1
            position = next_position
            guard_map[position[0]][position[1]] = 'X'
    else:
        break

print(result)
