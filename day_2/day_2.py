
def split(delimiters, string, maxsplit=0):
    import re
    regexPattern = '|'.join(map(re.escape, delimiters))
    return re.split(regexPattern, string, maxsplit)

f = open("input.txt", "r")

count_rule1_okay = 0
count_rule2_okay = 0

for line in f:
    data = split("- :\n", line)
    print(data)
    minrep = int(data[0])
    maxrep = int(data[1])
    letter = data[2]
    password = data[4]
    count = password.count(letter)
    if count >= minrep and count <= maxrep:
        count_rule1_okay += 1

    if (password[minrep-1] == letter) ^ (password[maxrep-1] == letter):
        count_rule2_okay += 1

print(count_rule1_okay)
print(count_rule2_okay)




