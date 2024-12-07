import re
with open('7/input.txt', 'r') as f:
    input_str = f.read().strip()

result = 0


def ternary(n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))    


def evaluate(num1, num2, operator):
    if operator == '0':
        return num1 + num2
    elif operator == '1':
        return num1 * num2
    elif operator == '2':
        return int(str(num1) + str(num2))
    else:
        raise ValueError


for line in input_str.split('\n'):
    test_value = line.split(':')[0]
    nums = [int(x) for x in line.split(':')[1].strip().split(' ')]
    for i in range(pow(3, len(nums) - 1)):
        operators = ternary(i)
        operators = '0' * (len(nums) - 1 - len(operators)) + operators
        this_result = nums[0]
        for n in range(1, len(nums)):
            this_result = evaluate(this_result, nums[n], operators[n - 1])
        if this_result == int(test_value):
            result += this_result
            break

        
print(result)
