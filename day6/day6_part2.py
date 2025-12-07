f = open("day6_input.txt")
lines = f.readlines()
lines = [x.replace("\n","") for x in lines]
operators = [lines[-1]]

total = 0
numbers = []
print(len(lines)-1)
for i in reversed(range(len(lines[0]))):
    print("\nCurrent Column : " + str(i))

    j = 0
    number = 0
    char = lines[j][i]
    while char != '*' and char != '+' and j != len(lines)-1: 
        print("j-st character in in this column : " + str(char))    
        if char == ' ':
            j += 1
        elif char == '*' or char == '+':
            break
        else:
            number = number*10 + int(char)
            print("Current building this number : " + str(number))
            j += 1
        char = lines[j][i] 


    if  char == '*' or char == '+':
        print("Operator found : " + char)
        numbers.append(number)
        if char == "*":
            print("Multiplying all number in : " + str(numbers))
            subtotal = 1
            for num in numbers:
                subtotal *= num
        else:
            print("Adding all number in : " + str(numbers))
            subtotal = 0
            for num in numbers:
                subtotal += num
        print("Adding subtotal : " + str(subtotal))
        total += subtotal
        numbers = []

    else:
        print("\nEnd of column reached : This is the final number : " + str(number))
        if number != 0:
            numbers.append(number)
print(total)

