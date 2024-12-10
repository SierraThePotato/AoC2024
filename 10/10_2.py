with open('10/input.txt', 'r') as f:
    input_str = f.read().strip()


trailheads = []
tmap = [[int(y)for y in x] for x in input_str.split('\n')]

# find trailheads
for i in range(len(tmap)):
    for j in range(len(tmap[i])):
        if tmap[i][j] == 0:
            trailheads.append((i, j))



def find_end(prev_i, prev_j, i, j, score):
    if i > (len(tmap) - 1) or i < 0 or j > (len(tmap[0]) - 1) or j < 0:
        return 0
    if not (prev_i == i and prev_j == j) and tmap[prev_i][prev_j] != tmap[i][j] - 1:
        return 0
    if tmap[i][j] == 9:
        return 1
    return find_end(i, j, i - 1, j, score) + find_end(i, j, i + 1, j, score) + find_end(i, j, i, j - 1, score) + find_end(i, j, i, j + 1, score) 

result = 0

for thead in trailheads:
    result += find_end(thead[0], thead[1], thead[0], thead[1], (thead[0], thead[1]))


print(result)
