with open("day1_input.txt") as f:
    status = 50
    total = 0
    for line in f.readlines():
        letter = line[0]
        if letter == 'L':
            status = (status - int(line[1:]) ) % 100
        else:
            status = (status + int(line[1:]) ) % 100
        if status == 0:
            total += 1
print(total)


