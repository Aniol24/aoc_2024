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

print(len(mem))
print(mem)

for ab in range(len(mem)-1, -1, -1):
    if(actualIndex > ab):
        print(actualIndex, ab)
        break
    
    if mem[ab] != ".":
        while mem[actualIndex] != ".":
            if (actualIndex > ab):
                break
            actualIndex += 1
        if(actualIndex > ab):
            break
            
        if(actualIndex < len(mem)):
            mem[actualIndex] = mem[ab]
            mem[ab] = "."

sum = 0

for i in range(len(mem)):
    if mem[i] == ".":
        break
    else:
        sum += int(mem[i]) * i


print(sum)

