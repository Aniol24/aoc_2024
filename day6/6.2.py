import sys

input_file = "input.txt"

def read_input(input_file):
    with open(input_file, "r") as f:
        data = f.read()
    return data.strip()

mapa = read_input(input_file)
mapa = mapa.split("\n")
mapa_final = [list(row) for row in mapa]
mapa = [list(row) for row in mapa]

directions = ["UP", "RIGHT", "DOWN", "LEFT"]
directions_vectors = {"UP": (-1, 0), "RIGHT": (0, 1), "DOWN": (1, 0), "LEFT": (0, -1)}

def move90DegreesRight(current_direction):
    current_direction_index = directions.index(current_direction)
    new_direction_index = (current_direction_index + 1) % 4
    return directions[new_direction_index]

def find_starting_point(mapa):
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == "^":
                return i, j

sp = find_starting_point(mapa)

sum = 0

total_cells = len(mapa) * len(mapa[0])
processed_cells = 0
progress_bar_length = 50  

def update_progress_bar(current, total, bar_length=50):
    progress = current / total
    block = int(progress * bar_length)
    bar = "#" * block + "-" * (bar_length - block)
    sys.stdout.write(f"\r[{bar}] {progress * 100:.2f}%")
    sys.stdout.flush()

#THIS SOLUTION IS NOT OPTIMAL (IT TAKES A LOT OF TIME TO FINISH) SO I ADDED A PROGRESS BAR TO SEE HOW IT IS GOING (AND MAKE IT SLOWER :D)

for i in range(len(mapa)):
    for j in range(len(mapa[i])):
        processed_cells += 1
        update_progress_bar(processed_cells, total_cells, progress_bar_length)

        actual_symbol = mapa[i][j]
        if actual_symbol != "^":
            mapa[i][j] = "#"

        if actual_symbol == "#":
            continue

        cc = sp
        current_direction = "UP"
        is_inside = True

        visited_states = set()

        while is_inside:
            current_state = (cc, current_direction)
            if current_state in visited_states:
                sum += 1
                is_inside = False
            visited_states.add(current_state)

            next_row = cc[0] + directions_vectors[current_direction][0]
            next_col = cc[1] + directions_vectors[current_direction][1]

            if next_row < 0 or next_row >= len(mapa) or next_col < 0 or next_col >= len(mapa[0]):
                is_inside = False
            elif mapa[next_row][next_col] == "#":
                current_direction = move90DegreesRight(current_direction)
            else:
                cc = (next_row, next_col)

        mapa[i][j] = actual_symbol

sys.stdout.write("\n")
print(f"Final Sum: {sum}")
