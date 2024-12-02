# Input data: https://adventofcode.com/2024/day/1/input

data = open("2024/1/data.txt").read().split("\n")

total = 0

leftList = []
rightList = []
for index,item in enumerate(data):
    leftList.append(item.split(" ")[0])
    rightList.append(item.split(" ")[3])

for index,item in enumerate(leftList):
    total += int(item) * rightList.count(item)

print(total)