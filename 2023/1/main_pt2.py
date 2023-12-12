data = open("2023/1/data.txt").read().split("\n")

total = 0
for index,value in enumerate(data):
    values = []
    indexes = []
    for cindex,cvalue in enumerate(value):
        if cvalue.isnumeric():
            values.append(int(cvalue))
            indexes.append(int(cindex))
    index = 0
    while True:
        if value.find("one", index) != -1:
            values.append(1)
            indexes.append(value.find("one", index))
            index = value.find("one", index) + 3
        else:
            index = 0
            break
    while True:
        if value.find("two", index) != -1:
            values.append(2)
            indexes.append(value.find("two", index))
            index = value.find("two", index) + 3
        else:
            index = 0
            break
    while True:
        if value.find("three", index) != -1:
            values.append(3)
            indexes.append(value.find("three", index))
            index = value.find("three", index) + 3
        else:
            index = 0
            break
    while True:
        if value.find("four", index) != -1:
            values.append(4)
            indexes.append(value.find("four", index))
            index = value.find("four", index) + 3
        else:
            index = 0
            break
    while True:
        if value.find("five", index) != -1:
            values.append(5)
            indexes.append(value.find("five", index))
            index = value.find("five", index) + 3
        else:
            index = 0
            break
    while True:
        if value.find("six", index) != -1:
            values.append(6)
            indexes.append(value.find("six", index))
            index = value.find("six", index) + 3
        else:
            index = 0
            break
    while True:
        if value.find("seven", index) != -1:
            values.append(7)
            indexes.append(value.find("seven", index))
            index = value.find("seven", index) + 3
        else:
            index = 0
            break
    while True:
        if value.find("eight", index) != -1:
            values.append(8)
            indexes.append(value.find("eight", index))
            index = value.find("eight", index) + 3
        else:
            index = 0
            break
    while True:
        if value.find("nine", index) != -1:
            values.append(9)
            indexes.append(value.find("nine", index))
            index = value.find("nine", index) + 3
        else:
            index = 0
            break

    if len(values) == 1:
        total += int(f"{values[0]}{values[0]}")
    else:
        total += int(f"{values[indexes.index(min(indexes))]}{values[indexes.index(max(indexes))]}")

print(total)