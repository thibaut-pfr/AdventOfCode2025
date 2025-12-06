
def FindBiggestInLine(s, bestValues=[0]*12, j=0):

    if len(s) == 1:
        if int(s) > bestValues[-1]:
            bestValues[-1] = int(s)
            
        return int("".join(str(d) for d in bestValues))

    if len(s) <= 11:
        j += 1
    else :
        j = 0

    head = int(s[0])

    i = j
    while i < 12:
        if bestValues[i] < head:
            bestValues[i] = head
            bestValues[i+1:] =[0] * (12 - (i+1))
            break
        i += 1

    return FindBiggestInLine(s[1:], bestValues=bestValues, j=j)


f = open("day3_part1_input.txt")
total = 0
for line in f.readlines():
    line = line.strip()
    biggest = FindBiggestInLine(line[1:], bestValues=[int(line[0]),0,0,0,0,0,0,0,0,0,0,0], j=0)
    total += biggest
print(total)

