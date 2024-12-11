input_file = "input.txt"

def read_input(input_file):
    with open(input_file, "r") as f:
        data = f.read()
    return data.strip()


data = read_input(input_file)
data = data.split("\n")
calibrations = []
for line in data:
    calibrations.append(line.split(","))


def checkBacktracking(numbers, array, max_num, actual_index):
    sum = numbers[0]
    for i in range(actual_index):
        if array[i] == 0:
            sum += numbers[i + 1]
        else:
            sum = numbers[i + 1] * sum
        if(sum > max_num):
            return False
    return True
    

def backtracking(numbers, array, max_num, index):
    global solution_exists

    if index == len(array):
        sum = numbers[0]
        for i in range(len(array)):
            if array[i] == 0:
                sum += numbers[i + 1]
            else:
                sum = numbers[i + 1] * sum
        if sum == max_num:
            solution_exists = True
        return

    for i in range(1):
        array[index] = i
        if checkBacktracking(numbers, array, max_num, index):
            backtracking(numbers, array, max_num, index + 1)

sum = 0

for calibration in calibrations:
    actual_c = calibration[0]
    actual_c = actual_c.split(":")
    max_num = int(actual_c[0])
    numbers = actual_c[1].split(" ")
    numbers.pop(0)
    solution_exists = False
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])

    backtracking(numbers, [0] * (len(numbers) - 1), max_num, 0)
    if solution_exists:
        sum += max_num

print(sum)  
