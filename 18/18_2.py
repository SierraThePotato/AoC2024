import heapq
with open('18/input.txt', 'r') as f:
    input_str = f.read().strip()


blocks = [(int(x.split(',')[0]), int(x.split(',')[1])) for x in input_str.split('\n')]

mem = [['.' for _ in range(71)] for x in range(71)]
# mem = [['.' for _ in range(7)] for x in range(7)]

start = (0, 0)
finish = (70, 70)
# finish = (6, 6)


def find_path():

    pq = []
    heapq.heappush(pq, (start[0], start[1], 0))
    visited = {(start[0], start[1]): 0}

    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

    while pq:
        i, j, steps = heapq.heappop(pq) 

        if (i, j) == finish:
            return True
        
        for d in range(4):
            ni, nj = i + directions[d][0], j + directions[d][1]
            if 0 <= ni < len(mem) and 0 <= nj < len(mem[0]) and mem[ni][nj] != '#':
                nsteps = steps + 1
                if (ni, nj) not in visited or visited[(ni, nj)] > nsteps:
                    visited[(ni, nj)] = nsteps
                    heapq.heappush(pq, (ni, nj, nsteps))
    
    return False




# falling bytes
n = 0
while n < len(blocks):
    b = blocks[n]
    i, j = b[1], b[0]
    mem[i][j] = '#'
    n += 1
    if not find_path():
        break

result = blocks[n - 1]

print(f'{result[0]},{result[1]}')