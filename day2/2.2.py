input = "input.txt"

def read_input(input):

    with open(input, "r") as f:
        data = f.read() 

    return data  

def split_array(input_array, chunk_size):
    return [input_array[i:i + chunk_size] for i in range(0, len(input_array), chunk_size)]  

def isSortedUpOrDown(array):
    if all(array[i] < array[i + 1] for i in range(len(array) - 1)):
        return True
    if all(array[i] > array[i + 1] for i in range(len(array) - 1)):
        return True
    return False

def check_array_sorting(arr):
    ascending = True
    descending = True
    broken_indices = []

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            ascending = False
            if descending:  
                broken_indices.append(i + 1)
        elif arr[i] < arr[i + 1]:
            descending = False
            if ascending:
                broken_indices.append(i + 1)

    if not ascending and not descending:
        arr.pop(broken_indices[0])
        return isSortedUpOrDown(arr)
    else:
        return True
  
def differenceChecker(array, smallest, biggest):
    for i in range(len(array) - 1):
        if( abs(array[i] - array[i + 1]) <= smallest or abs(array[i] - array[i + 1]) > biggest):
            return False
    return True

def check_array_difference(array, smallest, biggest):
    for i in range(len(array) - 1):
        if( abs(array[i] - array[i + 1]) <= smallest or abs(array[i] - array[i + 1]) > biggest):
            array.pop(i)
            return differenceChecker(array, smallest, biggest)
             
    return True

data = read_input(input)

reports = [list(map(int, line.split())) for line in data.strip().split('\n')]

reports_results = [True] * len(reports)

for i in range(len(reports)):


    if check_array_sorting(reports[i]) == True and check_array_difference(reports[i], 0, 3) == True:
        reports_results[i] = True
    else:
        reports_results[i] = False

print(reports_results.count(True))    

