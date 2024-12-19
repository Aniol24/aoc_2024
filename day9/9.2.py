input_file = "input.txt"

def read_input(input_file):
    with open(input_file, "r") as f:
        data = f.read()
    return data.strip()


data = read_input(input_file)
mem = []
index=0

for i in range(len(data)):
    if i % 2 == 0:
        for j in range(int(data[i])):
            mem.append(index)
        index += 1
    else:
        for j in range(int(data[i])):
            mem.append(".")

actualIndex = 0
actualNumber = mem[len(mem)-1]
length = 1




for ab in range(len(mem)-1, -1, -1):
    if mem[ab] != actualNumber:
        searchForLengthComb(length, actualNumber, ab)

print(sum)

