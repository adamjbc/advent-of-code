import re

f = open("input.txt", "r")

all_data = []

for line in f:
    entries = line.rstrip().split(" ")
    all_data += entries


passports = list()
passport = dict()

for entry in all_data:
    if entry == "":
        passports.append(passport)
        passport = dict()
    else:
        [key, value] = entry.split(":")
        passport[key] = value

passports.append(passport)


count_valid = 0

for passport in passports:
    if len(passport) == 8:
        count_valid += 1
    elif len(passport) == 7 and "cid" not in passport:
        count_valid += 1
    else:
        count_valid += 0

print(count_valid)


count_valid = 0

for passport in passports:
    if len(passport) < 7 or (len(passport) == 7 and "cid" in passport):
        print(f"invalid")
        continue
    
    try:
        byr = int(passport["byr"])
        if (byr < 1920) or (byr > 2002):
            print(f"byr invalid {byr}")
            continue
    except ValueError:
        print(f"byr invalid {byr}")
        continue

    try:
        iyr = int(passport["iyr"])
        if (iyr < 2010) or (iyr > 2020):
            print(f"iyr invalid {iyr}")
            continue
    except ValueError:
        print(f"iyr invalid {iyr}")
        continue

    try:
        eyr = int(passport["eyr"])
        if (eyr < 2020) or (eyr > 2030):
            print(f"eyr invalid {eyr}")
            continue
    except ValueError:
        print(f"eyr invalid {eyr}")
        continue

    try:
        hgt = int(passport["hgt"][:-2])
        if (passport["hgt"][-2:] == "cm") and ((hgt < 150) or (hgt > 193)):
            print(f"hgt invalid a {hgt}")
            continue
        if (passport["hgt"][-2:] == "in") and ((hgt < 59) or (hgt > 76)):
            print(f"hgt invalid b {hgt}")
            continue
        if not ((passport["hgt"][-2:] == "cm") or (passport["hgt"][-2:] == "in")):
            print(f"hgt invalid c {hgt}")
            continue
    except ValueError:
        print(f"hgt invalid d {passport['hgt']}")
        continue

    if not re.search("^#([a-fA-F0-9]{6})$", passport['hcl']):
        print(f"hcl invalid {passport['hcl']}")
        continue

    if not passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        print(f"ecl invalid {passport['ecl']}")
        continue

    if not re.search("^([0-9]{9})$", passport['pid']):
        print(f"pid invalid {passport['pid']}")
        continue

    print("VALID")
    count_valid += 1

print(count_valid)




