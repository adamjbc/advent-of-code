
f = open("input.txt", "r")

def get_row(code, seats):
    if code == "":
        return seats[0]
    else:
        if code[0] == "F":
            return get_row(code[1:], seats[0:int(len(seats)/2)])
        elif code[0] == "B":
            return get_row(code[1:], seats[int(len(seats)/2):])
    

def get_col(code, seats):
    if code == "":
        return seats[0]
    else:
        if code[0] == "L":
            return get_col(code[1:], seats[0:int(len(seats)/2)])
        elif code[0] == "R":
            return get_col(code[1:], seats[int(len(seats)/2):])


max_seat = 0

all_seats = list(range(0, 865))

for line in f:
    row = get_row(line.rstrip()[0:7], range(0, 128))
    col = get_col(line.rstrip()[7:10], range(0, 8))

    print(row)
    print(col)

    seat = row * 8 + col

    if seat > max_seat:
        max_seat = seat

    all_seats.remove(seat)




print(get_row("BFFFBBF", range(0, 128)))
print(get_row("FFFBBBF", range(0, 128)))
print(get_row("BBFFBBF", range(0, 128)))

print(get_col("RRR", range(0, 8)))
print(get_col("RRR", range(0, 8)))
print(get_col("RLL", range(0, 8)))

print(max_seat)

print(all_seats)

