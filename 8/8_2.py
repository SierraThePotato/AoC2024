from itertools import product
with open('8/input.txt', 'r') as f:
    input_str = f.read().strip()


antennas = {}
antinodes = set()

antenna_map = [[y for y in x] for x in input_str.split('\n')]

for i in range(len(antenna_map)):
    for j in range(len(antenna_map[i])):
        if antenna_map[i][j] != '.':
            if antenna_map[i][j] not in antennas.keys():
                antennas[antenna_map[i][j]] = []
            antennas[antenna_map[i][j]].append((i, j))


for keys, values in antennas.items():
    for a in product(values, values):
        if a[0] == a[1]:
            continue
        vector = (a[0][0] - a[1][0], a[0][1] - a[1][1])
        # direction 1
        a1 = a[0]
        antinodes.add(a1)
        while True:
            a1 = (a1[0] + vector[0], a1[1] + vector[1])
            if 0 <= a1[0] < len(antenna_map) and 0 <= a1[1] < len(antenna_map[0]):
                antinodes.add(a1)
            else:
                break
        # direction 2
        a2 = a[1]
        antinodes.add(a2)
        while True:
            a2 = (a2[0] - vector[0], a2[1] - vector[1])
            if 0 <= a2[0] < len(antenna_map) and 0 <= a2[1] < len(antenna_map[0]):
                antinodes.add(a2)
            else:
                break

print(len(antinodes))
