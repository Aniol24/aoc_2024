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

def differenceChecker(array, smallest, biggest):
    for i in range(len(array) - 1):
        if( abs(array[i] - array[i + 1]) <= smallest or abs(array[i] - array[i + 1]) > biggest):
            return False
    return True

data = read_input(input)

reports = [list(map(int, line.split())) for line in data.strip().split('\n')]

reports_results = [True] * len(reports)

for i in range(len(reports)):

    if isSortedUpOrDown(reports[i]) == True and differenceChecker(reports[i], 0, 3) == True:
        reports_results[i] = True
    else:
        reports_results[i] = False
        

print(reports_results.count(True))    

