f = open("day6_input.txt")
lines = []
readlines = f.readlines()
for line in readlines[:-1]:
    line = line.strip().split()
    line = [x.strip() for x in line]
    lines.append(list(map(int,line)))
operators = [x for x in readlines[-1].strip().split() if x != '']


total = 0
for i in range(len(operators)):
    print("\nCurrent Column : " + str(i))
    operator = operators[i]
    print("Operator : " + operator)
    if operator == "*":
        subtotal = 1
        for j in range(len(readlines)-1):
            subtotal *= lines[j][i]

    else:
        subtotal = 0
        for j in range(len(readlines)-1):
            subtotal += lines[j][i]

    print("Subtotal for this column : " + str(subtotal))
    total += subtotal
print(total)
