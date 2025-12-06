f = open("day4_input.txt")
matrix = []
for line in f.readlines():
    line = line.strip()
    matrix.append(list(line))

row_length = len(matrix)
col_length = len(matrix[0])

print("Dimensions : " + str(row_length) + " x " + str(col_length))

total = 0

for row in range(row_length):
    for col in range(col_length):
        if matrix[row][col] == '.':
            continue
        else:
            print("\nCurrent elem (" + str(row) + ", " + str(col) + str(")"))
            count = 0
            directions = [(1,-1), (0,-1), (-1,-1), (0,1), (1,0), (-1,0), (1,1), (-1,1)]

            if row == 0 and col == 0:
                remove = [(1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]
                directions = [x for x in directions if x not in remove]

            elif row == row_length-1 and col == col_length-1:
                remove = [(1,1), (0,1), (-1,1), (1,0), (1,-1)]
                directions = [x for x in directions if x not in remove]
            
            elif row == row_length-1 and col == 0:
                remove = [(1,-1), (1,0), (1,1), (-1,-1), (0,-1)]
                directions = [x for x in directions if x not in remove]

            elif row == 0 and col == col_length-1:
                remove = [(-1,-1), (-1,0), (1,1), (-1,1), (0,1)]
                directions = [x for x in directions if x not in remove]

            elif row == 0:
                remove = [(-1,1), (-1,0), (-1,-1)]
                directions = [x for x in directions if x not in remove]

            elif col == 0:
                remove = [(-1,-1), (0,-1), (1,-1)]
                directions = [x for x in directions if x not in remove]

            elif row == row_length-1:
                remove = [(1,-1), (1,0), (1,1)]
                directions = [x for x in directions if x not in remove]

            elif col == col_length-1:
                remove = [(-1,1), (0,1), (1,1)]
                directions = [x for x in directions if x not in remove]
                
            for dir in directions:
                print("Checking element (" + str(row+dir[0]) + ", " + str(col+dir[1]) + str(")") + " : This is a '" + matrix[row+dir[0]][col+dir[1]], end="' ")
                if matrix[row+dir[0]][col+dir[1]] == '@':
                    print("Count +1 = " + str(count+1))
                    count += 1
                else :
                    print("\n")

            print("Final count : " + str(count))
            if count < 4 :
                print("Count < 4 :  total +1 = " + str(total+1))
                total += 1

print(total)


