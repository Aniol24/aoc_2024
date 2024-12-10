input = "input.txt"

def read_input(input):

    with open(input, "r") as f:
        data = f.read() 

    return data    

data = read_input(input)

numbers = list(filter(lambda x: x.isdigit(), data.split()))

array1 = []
array2 = []

for i in range(len(numbers)):
        if i % 2 == 0:
            array1.append(numbers[i])
        else:
            array2.append(numbers[i])

array_left = [int(string_number) for string_number in array1]
array_right = [int(string_number) for string_number in array2]

array_left.sort()
array_right.sort()

final_array = []

for i in range(len(array1)):
    final_array.append(abs(array_left[i] - array_right[i]))

sum = 0
for i in range(len(final_array)):
    sum = sum + final_array[i]

print(sum)
