with open('14/input.txt', 'r') as f:
    input_str = f.read().strip()


robots = [([int(x) for x in r.split(' ')[0].lstrip('p=').split(',')], [int(x) for x in r.split(' ')[1].lstrip('v=').split(',')]) for r in input_str.split('\n')]


mapx = 101
mapy = 103

seconds = 0

while True:
    visual = [['.' for x in range(mapx)] for _ in range(mapy)]
    for r in robots:
        r[0][0] = (r[0][0] + r[1][0]) % mapx 
        r[0][1] = (r[0][1] + r[1][1]) % mapy
        visual[r[0][1]][r[0][0]] = '#'
    str_vis = '\n'.join([''.join(x) for x in visual])
    print(str_vis)
    seconds += 1
    print(seconds)
    if '############' in str_vis:
        break
    
