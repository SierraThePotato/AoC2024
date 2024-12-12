with open('12/input.txt', 'r') as f:
    input_str = f.read().strip()

result = 0

farm = [[y for y in x] for x in input_str.split('\n')]

visited = []

groups = {}


def get_group(i, j, group_key):
    if i < 0 or i >= len(farm) or j < 0 or j >= len(farm[0]):
        return []
    if farm[i][j] != group_key:
        return []
    if (i, j) in visited:
        return []
    visited.append((i, j))
    return [(i, j)] + get_group(i - 1, j, group_key) +  get_group(i + 1, j, group_key) + get_group(i, j - 1, group_key) + get_group(i, j + 1, group_key)


def get_perimeter(group):
    all_perimeter = 0
    for tile in group:
        perimeter = 4
        if (tile[0] - 1, tile[1]) in group:
            perimeter -= 1
        if (tile[0] + 1, tile[1]) in group:
            perimeter -= 1
        if (tile[0], tile[1] - 1) in group:
            perimeter -= 1
        if (tile[0], tile[1] + 1) in group:
            perimeter -= 1
        all_perimeter += perimeter
    return all_perimeter
        

group_id = 0
for i in range(len(farm)):
    for j in range(len(farm[0])):
        if (i, j) not in visited:
            groups[group_id] = get_group(i, j, farm[i][j])
            group_id += 1


for key, values in groups.items():
    result += len(values) * get_perimeter(values)


print(result)
