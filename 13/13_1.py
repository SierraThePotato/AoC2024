with open('13/input.txt', 'r') as f:
    input_str = f.read().strip()

result = 0

machines_input = [x.split('\n') for x in input_str.split('\n\n')]

machines = []

for m in machines_input:
    for i in range(3):
        a = [int(c.split('+')[1]) for c in m[0].split(': ')[1].split(', ')]
        b = [int(c.split('+')[1]) for c in m[1].split(': ')[1].split(', ')]
        p = [int(c.split('=')[1]) for c in m[2].split(': ')[1].split(', ')]
    machines.append((a, b, p))

for m in machines:
    costs = []
    for a_n in range(101):
        for b_n in range(101):
            x = a_n * m[0][0] + b_n * m[1][0]
            y = a_n * m[0][1] + b_n * m[1][1]
            if [x, y] == m[2]:
                costs.append(3 * a_n + b_n)
    if len(costs) > 0:
        result += min(costs)

print(result)
