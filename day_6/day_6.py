
f = open("input.txt")

count_1 = 0
count_2 = 0

working = list()

for line in f:
    if line == "\n":
        print(working)
        count_1 += len(set().union(*working))
        count_2 += len(set(working[0]).intersection(*working))
        working = list()
    else:
        working.append(set(line.rstrip()))

count_1 += len(set().union(*working))
count_2 += len(set(working[0]).intersection(*working))

print(count_1)
print(count_2)
