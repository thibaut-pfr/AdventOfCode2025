def countNrOfZeros(start, input):
    nrOfZeros = 0

    direction = input[0]
    toTurn = int(input[1:])

    #print("Angle before : " + str(start))

    fullRotation = toTurn // 100
    rest = toTurn % 100
    nrOfZeros += fullRotation
    #print("Number of full rotations : " + str(fullRotation))
    #print("Still left to turn : " + str(rest))

    if direction == 'R':
        if rest >= 100 - start :
            nrOfZeros += 1
            #print("+1")
        start = (start + rest) % 100

    else :
        if rest >= start and start != 0:
            nrOfZeros += 1
            #print("+1")
        start = (start - rest) % 100

    #print("Angle after : " + str(start))
    return start, nrOfZeros

with open("day1_input.txt") as f:
    lockAngle = 50
    zerosCount = 0
    for line in f.readlines():
        #print("\nLine : " + line, end="")
        a,b = countNrOfZeros(lockAngle, line)
        lockAngle = a
        zerosCount += b 

print("Total zeros encountered : " + str(zerosCount))

