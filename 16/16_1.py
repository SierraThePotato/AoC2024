import heapq


with open('16/input.txt', 'r') as f:
    input_str = f.read().strip()


track = [list(x) for x in input_str.split('\n')]

moves = [(-1, 0), (0, 1), (1, 0), (0, -1)] # N E S W

# find start and finish
deer = [len(track) - 2, 1]
finish = (1, len(track[1]) - 2)


pq = [(0, deer[0], deer[1], 1)]

visited = {}
visited[(deer[0], deer[1], 1)] = 0

result = 0

while pq:
    score, i, j, direction = heapq.heappop(pq)

    if (i, j) == finish:
        result = score
        break

    # forward
    di, dj = moves[direction]
    ni, nj = i + di, j + dj

    if 0 <= ni < len(track) and 0 <= nj < len(track[0]) and track[ni][nj] != '#':
        nscore = score + 1
        if (ni, nj, direction) not in visited or visited[(ni, nj, direction)] > nscore:
            visited[(ni, nj, direction)] = nscore
            heapq.heappush(pq, (nscore, ni, nj, direction))

    # right 
    ndirection = (direction + 1) % 4
    nscore = score + 1000
    if (i, j, ndirection) not in visited or visited[(i, j, ndirection)] > nscore:
        visited[(i, j, direction)] = nscore
        heapq.heappush(pq, (nscore, i, j, ndirection))

    # left 
    ndirection = (direction - 1 + 4) % 4
    nscore = score + 1000
    if (i, j, ndirection) not in visited or visited[(i, j, ndirection)] > nscore:
        visited[(i, j, direction)] = nscore
        heapq.heappush(pq, (nscore, i, j, ndirection))


print(result)
