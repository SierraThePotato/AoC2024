
with open('1/input.txt', 'r') as f:
    input_str = f.read()

list1 = []
list2 = []

for line in input_str.split('\n'):
    list1.append(int(line.split('   ')[0]))
    list2.append(int(line.split('   ')[1]))

result = 0

for _ in range(len(list1)):
    min1 = min(list1)
    list1.remove(min1)
    min2 = min(list2)
    list2.remove(min2)
    result += abs(min1 - min2)

print(result)
