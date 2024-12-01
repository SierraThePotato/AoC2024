
with open('1/input.txt', 'r') as f:
    input_str = f.read()

list1 = []
list2 = []

for line in input_str.split('\n'):
    list1.append(int(line.split('   ')[0]))
    list2.append(int(line.split('   ')[1]))

result = 0

for n in list1:
    result += n * list2.count(n)

print(result)