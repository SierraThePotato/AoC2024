with open('14/input.txt', 'r') as f:
    input_str = f.read().strip()


robots = [([int(x) for x in r.split(' ')[0].lstrip('p=').split(',')], [int(x) for x in r.split(' ')[1].lstrip('v=').split(',')]) for r in input_str.split('\n')]

mapx = 101
mapy = 103

for r in robots:
    r[0][0] = (r[0][0] + 100 * r[1][0]) % mapx 
    r[0][1] = (r[0][1] + 100 * r[1][1]) % mapy

quads = [0, 0, 0, 0]
for r in robots:
    x, y = r[0][0], r[0][1]
    if x < (mapx-1)/2 and y < (mapy-1)/2:
        quads[0] += 1
    elif x > (mapx-1)/2 and y < (mapy-1)/2:
        quads[1] += 1
    elif x < (mapx-1)/2 and y > (mapy-1)/2:
        quads[2] += 1
    elif x > (mapx-1)/2 and y > (mapy-1)/2:
        quads[3] += 1


print(quads[0] * quads[1] * quads[2] * quads[3])
