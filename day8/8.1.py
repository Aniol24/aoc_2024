input_file = "input.txt"

def read_input(input_file):
    with open(input_file, "r") as f:
        data = f.read()
    return data.strip()


data = read_input(input_file)
data = data.split("\n")
global hashMap
hashMap = [list(row) for row in data]

def radiate(data, i, j):
    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[x][y] == data[i][j] and (x != i or y != j):
                dx = x - i
                dy = y - j
                nx = x + dx
                ny = y + dy
                if nx >= 0 and nx < len(data) and ny >= 0 and ny < len(data[nx]):
                    hashMap[nx][ny] = "#"
                
                
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] != ".":
            radiate(data, i, j)

hashMap = "\n".join("".join(row) for row in hashMap)
hashMap = hashMap.count("#")
print(hashMap)

