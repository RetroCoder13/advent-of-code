# Input data: https://adventofcode.com/2023/day/3/input

data = open("2023/3/data.txt").read().split("\n")

start = None
count = 0
total = 0
for index,value in enumerate(data):
    for cindex,character in enumerate(value):
        if character.isnumeric():
            if start == None:
                start = cindex
            count += 1
        else:
            symbol = False
            for x in range(count+2):
                for y in range(3):
                    try:
                        if y+index-1 >= 0 and x+start-1 >= 0 and y+index-1 < len(data) and x+start-1 < len(value):
                            if(data[y+index-1][x+start-1] != "." and not data[y+index-1][x+start-1].isnumeric()):
                                symbol = True
                    except:
                        continue
            if symbol:
                number = ""
                for i in range(count):
                    number += value[start+i]
                total += int(number)
            start = None
            count = 0
    symbol = False
    for x in range(count+2):
        for y in range(3):
            try:
                if y+index-1 >= 0 and x+start-1 >= 0 and y+index-1 < len(data) and x+start-1 < len(value):
                    if(data[y+index-1][x+start-1] != "." and not data[y+index-1][x+start-1].isnumeric()):
                        symbol = True
            except:
                continue
    if symbol:
        number = ""
        for i in range(count):
            number += value[start+i]
        total += int(number)
    start = None
    count = 0
print(total)