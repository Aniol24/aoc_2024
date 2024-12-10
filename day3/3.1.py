import re 

input = "input.txt"

def read_input(input):

    with open(input, "r") as f:
        data = f.read() 

    return data  

data = read_input(input)
matches = re.findall(r"mul\(\d+,\d+\)", data)
sum = 0

for i in matches:
    i = i.split("(")[1].split(")")[0].split(",")
    int(i[0])
    int(i[1])
    sum = sum + int(i[0]) * int(i[1])
print(sum)




