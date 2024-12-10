input_file = "input.txt"

def read_input(input_file):
    with open(input_file, "r") as f:
        data = f.read()
    return data.strip()

data = read_input(input_file)

lines = data.split('\n')
WORD = "MAS"

def mirarCreu(row, column):
    directions = [  
        (-1, -1), 
        (-1, 1), 
        (1, -1), 
        (1, 1)  
    ]

    diagonal1 = []
    diagonal2 = []

    if( row == 0 or row == len(lines) - 1 or column == 0 or column == len(lines[row]) - 1 ):
        return 0

    diagonal1.append(lines[row + directions[0][0]][column + directions[0][1]])
    diagonal1.append(lines[row + directions[3][0]][column + directions[3][1]])

    diagonal2.append(lines[row + directions[1][0]][column + directions[1][1]])
    diagonal2.append(lines[row + directions[2][0]][column + directions[2][1]])

    print("Row: ", row)
    print("Column: ", column)
    print("Diagonal 1: ", diagonal1)
    print("Diagonal 2: ", diagonal2)

    if( ( "M" in diagonal1 and "S" in diagonal1 ) and ( "M" in diagonal2 and "S" in diagonal2 ) ):
        return 1
    else:    
        return 0
    

total_occurrences = 0

for row in range(len(lines)):
    for column in range(len(lines[row])):
        if lines[row][column] == "A":
            occurrences = mirarCreu(row, column)
            if occurrences > 0:
                total_occurrences += occurrences

print(f"Total occurrences of {WORD}: {total_occurrences}")
