input_file = "input.txt"

def read_input(input_file):
    with open(input_file, "r") as f:
        data = f.read()
    return data.strip()

data = read_input(input_file)
data = data.split("\n")
ordrers = []
prints = []
doing_ordrers = True

for i in range(len(data)):
    if data[i] == "":
        doing_ordrers = False
        continue
    if doing_ordrers:
        ordrers.append(data[i])
    else:
        prints.append(data[i])

for i in range(len(ordrers)):
    ordrers[i] = ordrers[i].split("|")

for i in range(len(prints)):
    prints[i] = prints[i].split(",")

incorrect_prints = []

for line in prints:
    is_ok = True
    for order in ordrers:
        if(order[0] in line and order[1] in line):
            if(line.index(order[0]) > line.index(order[1])):
                temp = line[line.index(order[0])]
                line[line.index(order[0])] = line[line.index(order[1])] 
                line[line.index(order[1])] = temp
                is_ok = False
                break
    if not is_ok:
        incorrect_prints.append(line)

for line in incorrect_prints:
    fixed = False
    while not fixed:
        fixed = True
        for order in ordrers:
            if(order[0] in line and order[1] in line):
                if(line.index(order[0]) > line.index(order[1])):
                    fixed = False
                    temp = line[line.index(order[0])]
                    line[line.index(order[0])] = line[line.index(order[1])] 
                    line[line.index(order[1])] = temp
                    break

sum = 0

for line in incorrect_prints:
    sum += int(line[len(line)//2])              

print(sum)