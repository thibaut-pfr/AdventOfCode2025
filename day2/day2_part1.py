def checkValid(n):
    asStr = str(n)
    length = len(asStr)
    if length % 2 != 0:
        return True
    if asStr[:length//2] != asStr[length//2:]:
        return True
    return False

#for i in range(38593856,38593863):
#   print(str(i) + " is valid ? : " + str(checkValid(i)))

f = open("day2_input.txt")
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
