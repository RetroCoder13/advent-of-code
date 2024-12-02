# Input data: https://adventofcode.com/2024/day/1/input

data = open("2024/1/data.txt").read().split("\n")

total = 0

leftList = []
rightList = []
for index,item in enumerate(data):
    leftList.append(item.split(" ")[0])
    rightList.append(item.split(" ")[3])

for i in range(len(leftList)):
    minL = min(leftList)
    minR = min(rightList)
    total += abs(int(minL) - int(minR))
    leftList.pop(leftList.index(minL))
    rightList.pop(rightList.index(minR))

print(total)