with open('13/input.txt', 'r') as f:
    input_str = f.read().strip()

result = 0

machines_input = [x.split('\n') for x in input_str.split('\n\n')]

machines = []

for m in machines_input:
    for i in range(3):
        a = [int(c.split('+')[1]) for c in m[0].split(': ')[1].split(', ')]
        b = [int(c.split('+')[1]) for c in m[1].split(': ')[1].split(', ')]
        p = [int(c.split('=')[1]) + 10000000000000 for c in m[2].split(': ')[1].split(', ')]
    machines.append((a, b, p))

for m in machines:
    ax, ay = m[0][0], m[0][1]
    bx, by = m[1][0], m[1][1]
    px, py = m[2][0], m[2][1]

    b = (py*ax-px*ay)/(by*ax-bx*ay)
    a = (px -b*bx)/ax

    if a.is_integer() and b.is_integer():
        result += a * 3 + b

print(int(result))
