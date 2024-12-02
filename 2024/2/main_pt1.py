# Input data: https://adventofcode.com/2024/day/2/input

data = open("2024/2/data.txt").read().split("\n")

total = 0

for index,item in enumerate(data):
    vals = item.split(" ")
    print(vals)
    increasing = int(vals[0]) < int(vals[1])
    allow = True
    for i in range(len(vals)-1):
        if int(vals[i]) < int(vals[i+1]) and increasing == True and abs(int(vals[i])-int(vals[i+1])) <= 3 and abs(int(vals[i])-int(vals[i+1])) >= 1:
            continue
        elif int(vals[i]) > int(vals[i+1]) and increasing == False and abs(int(vals[i])-int(vals[i+1])) <= 3 and abs(int(vals[i])-int(vals[i+1])) >= 1:
            continue
        else:
            allow = False
            break
    if allow == True:
        print(index)
        total += 1

print(total)