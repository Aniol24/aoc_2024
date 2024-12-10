input_file = "input.txt"

def read_input(input_file):
    with open(input_file, "r") as f:
        data = f.read()
    return data.strip()

data = read_input(input_file)

lines = data.split('\n')
WORD = "XMAS"

def mirarCreu(row, column):
    directions = [
        (-1, 0),  
        (1, 0),  
        (0, -1),  
        (0, 1),   
        (-1, -1), 
        (-1, 1), 
        (1, -1), 
        (1, 1)  
    ]
    occurrences = 0

    for dr, dc in directions:
        found = True
        for i in range(len(WORD)):
            new_row = row + dr * i
            new_col = column + dc * i

            if (
                new_row < 0 or new_row >= len(lines) or
                new_col < 0 or new_col >= len(lines[new_row]) or
                lines[new_row][new_col] != WORD[i]
            ):
                found = False
                break

        if found:
            occurrences += 1
            direction_name = {
                (-1, 0): "up", (1, 0): "down", (0, -1): "left", (0, 1): "right",
                (-1, -1): "diagonal up left", (-1, 1): "diagonal up right",
                (1, -1): "diagonal down left", (1, 1): "diagonal down right"
            }

    return occurrences

total_occurrences = 0

for row in range(len(lines)):
    for column in range(len(lines[row])):
        if lines[row][column] == WORD[0]:
            occurrences = mirarCreu(row, column)
            if occurrences > 0:
                total_occurrences += occurrences

print(f"Total occurrences of {WORD}: {total_occurrences}")
