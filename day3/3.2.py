import re 

input = "input.txt"

def read_input(input):

    with open(input, "r") as f:
        data = f.read() 

    return data  

data = read_input(input)
matches = re.findall(r"(mul\(\d+,\d+\)|don't\(\)|do\(\))", data)
sum = 0

last = ""

for i in matches:
    if i == "don't()":
        last = "don't()"
        continue
    if i == "do()":
        last = "do()"
        continue
    else:
        if last == "don't()":
            continue
        if last == "do()" or last == "":
            i = i.split("(")[1].split(")")[0].split(",")
            int(i[0])
            int(i[1])
            sum = sum + int(i[0]) * int(i[1])
            last = ""
            print(i)

print(sum)




