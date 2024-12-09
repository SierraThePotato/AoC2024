with open('9/input.txt', 'r') as f:
    input_str = f.read().strip()


# interpret input
disk = []
file_id = 0
for i in range(0, len(input_str) - 1, 2):
    disk.append((file_id, int(input_str[i])))
    disk.append((-1, int(input_str[i + 1])))
    file_id += 1
i += 2
disk.append((file_id, int(input_str[i])))


# move files
for i in range(len(disk) - 1, 0, -1):
    if disk[i][0] != -1:
        j = 1
        while (j < i) and (disk[j][0] != -1 or disk[j][1] < disk[i][1]):
            j += 1
        if j < i:
            space_left = disk[j][1] - disk[i][1]
            disk[i], disk[j] = (-1, disk[i][1]), disk[i]
            if space_left > 0:
                disk.insert(j + 1, (-1, space_left))
        


# expand result
disk_expanded = []
for block in disk:
    for _ in range(block[1]):
        disk_expanded.append(block[0])


# get checksum
result = 0
for i in range(len(disk_expanded)):
    if disk_expanded[i] != -1:
        result += i * int(disk_expanded[i])


print(result)
 