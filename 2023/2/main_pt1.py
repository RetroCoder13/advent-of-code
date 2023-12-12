red, green, blue = 12, 13, 14
data = open("2023/2/data.txt").read().split("\n")

for index,value in enumerate(data):
    data[index] = value.split(":")
    data[index].pop(0)
    data[index] = data[index][0].split(";")
    for list in range(len(data[index])):
        data[index][list] = data[index][list].replace(",","").split(" ")

total = 0
for gameindex,gamevalue in enumerate(data):
    possibleGame = True
    for index,value in enumerate(gamevalue):
        for i in range(round((len(value)-1)/2)):
            amount = int(value[i*2+1])
            colour = value[i*2+2]
            if (colour == "red" and amount > red) or (colour == "green" and amount > green) or (colour == "blue" and amount > blue):
                possibleGame = False
    if possibleGame:
        total += gameindex+1

print(total)