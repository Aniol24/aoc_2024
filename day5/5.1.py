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

sum = 0

for line in prints:
    is_ok = True
    for order in ordrers:
        if(order[0] in line and order[1] in line):
            if(line.index(order[0]) > line.index(order[1])):
                is_ok = False
                break
    if is_ok:
        sum += int(line[len(line)//2])

print(sum)