# Input data: https://adventofcode.com/2023/day/1/input

data = open("2023/1/data.txt").read().split("\n")

total = 0
for index,value in enumerate(data):
    values = []
    for cindex,cvalue in enumerate(value):
        if cvalue.isnumeric():
            values.append(int(cvalue))
    if len(values) == 1:
        total += int(f"{values[0]}{values[0]}")
    else:
        total += int(f"{values[0]}{values[len(values)-1]}")

print(total)