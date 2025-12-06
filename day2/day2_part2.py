def checkValid(n):
    asStr = str(n)
    length = len(asStr)

    for size in range (1, length//2 +1):
        if length % size == 0:
            nrOfRepetitions = length // size
            comparator = asStr[:size]
            foundDifference = False
            #print("Comparator : " + comparator)
            for i in range (1, nrOfRepetitions):
                #print(asStr[i*size: (i+1)*size])
                isDifferent = asStr[i*size: (i+1)*size] != comparator
                if isDifferent:
                    foundDifference = True
            if not foundDifference:
                return False
    return True

#for i in range(38593856,38593863):
#   print(str(i) + " is valid ? : " + str(checkValid(i)))

f = open("day2_part1_input.txt")
input = f.readline()

invalid = []

ranges = input.split(",")
for r in ranges:
    start = int(r.split("-")[0])
    end = int(r.split("-")[1])
    for num in range(start,end+1):
        if not checkValid(num):
            print(str(num))
            invalid.append(num)
print("Sum of invalid ID's : " + str(sum(invalid)))

