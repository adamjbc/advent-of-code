

f = open("input.txt", "r")

trees = []

for line in f:
    trees.append(line.rstrip())


def count_trees(right, down, trees):
    height = len(trees)
    width = len(trees[0])
    
    pos_x = 0
    pos_y = 0

    count = 0

    while pos_y < height:
        if trees[pos_y][pos_x % width] == "#":
            count += 1
        pos_x += right
        pos_y += down

    return count

print(count_trees(3, 1, trees))


a = count_trees(1, 1, trees)
b = count_trees(3, 1, trees)
c = count_trees(5, 1, trees)
d = count_trees(7, 1, trees)
e = count_trees(1, 2, trees)

print(a*b*c*d*e)







