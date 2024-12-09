with open('9/input.txt', 'r') as f:
    input_str = f.read().strip()


# interpret input
disk = []

file_id = 0
for i in range(0, len(input_str) - 1, 2):
    for j in range(int(input_str[i])):
        disk.append(file_id)
    for j in range(int(input_str[i + 1])):
        disk.append(-1)
    file_id += 1
i += 2
for j in range(int(input_str[i])):
    disk.append(file_id)


# move files
j = len(disk) - 1
i = 0
while i < j:
    if disk[i] == -1:
        if disk[j] != -1:
            disk[i], disk[j] = disk[j], disk[i]
        else:
            j -= 1
    else:
        i += 1

# get checksum
result = 0
for i in range(len(disk)):
    if disk[i] == -1:
        break
    result += i * int(disk[i])


print(result)
