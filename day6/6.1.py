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

cc = find_starting_point(mapa)
current_direction = "UP"
is_inside = True

visited_states = set()

mapa_final[cc[0]][cc[1]] = "X"

while is_inside:
    next_row = cc[0] + directions_vectors[current_direction][0]
    next_col = cc[1] + directions_vectors[current_direction][1]
    
    if next_row < 0 or next_row >= len(mapa) or next_col < 0 or next_col >= len(mapa[0]):
        mapa_final[cc[0]][cc[1]] = "X"
        is_inside = False
    elif mapa[next_row][next_col] == "#":
        current_direction = move90DegreesRight(current_direction)
    else:
        cc = (next_row, next_col)
        mapa_final[cc[0]][cc[1]] = "X"

print("\n".join("".join(row) for row in mapa_final))
print(sum([row.count("X") for row in mapa_final]))