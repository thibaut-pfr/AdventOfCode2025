def FindBiggestInLine(s, bestTens=float("-inf"), bestUnits=float("-inf")):
    if len(s) == 1:
        if int(s) > bestUnits:
            bestUnits = int(s)
        return bestTens*10 + bestUnits
    head = int(s[0])
    if head > bestTens:
        bestTens = head
        bestUnits = 0
    elif head > bestUnits:
        bestUnits = head
    return FindBiggestInLine(s[1:], bestTens, bestUnits)

f = open("day3_input.txt")
total = 0
test = ["987654321111111",
"811111111111119",
"234234234234278",
"818181911112111"]
for line in f.readlines():
    line = line.strip()
    biggest = FindBiggestInLine(line[1:], bestTens=int(line[0]))
    print(biggest)
    total += biggest
print(total)