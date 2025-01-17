# Input data: https://adventofcode.com/2024/day/2/input

import copy

data = open("2024/2/data.txt").read().split("\n")

total = 0

def checkRow(vals,n):
    print(n,vals)
    if n > 1:
        return False
    increasing = int(vals[0]) < int(vals[1])
    for i in range(len(vals)-1):
        if int(vals[i]) < int(vals[i+1]) and increasing == True and abs(int(vals[i])-int(vals[i+1])) <= 3 and abs(int(vals[i])-int(vals[i+1])) >= 1:
            continue
        elif int(vals[i]) > int(vals[i+1]) and increasing == False and abs(int(vals[i])-int(vals[i+1])) <= 3 and abs(int(vals[i])-int(vals[i+1])) >= 1:
            continue
        else:
            vals1 = copy.deepcopy(vals)
            vals1.pop(i)
            vals.pop(i+1)
            return checkRow(vals1,n+1) or checkRow(vals,n+1)
    return True

for index,item in enumerate(data):
    vals = item.split(" ")
    if checkRow(vals,0) == True:
        total += 1
    else:
        print(False)

print(total)