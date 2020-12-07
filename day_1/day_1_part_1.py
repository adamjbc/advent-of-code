

f = open("input.txt", "r")

data = []

for line in f:
    data.append(int(line))


print(data)

for x in data:
    for y in data:
        if (x+y) == 2020:
            print (x*y)


for x in data:
    for y in data:
        for z in data:
            if (x+y+z) == 2020:
                print (x*y*z)

