f = open("day7_input.txt")
lines = f.readlines()
lines = [x.replace("\n", "") for x in lines]
lines = [list(line) for line in lines]
print(lines)

# FIND STARTING POINT
j = 0
char = lines[0][j]
while char != 'S':
    j += 1
    char = lines[0][j]

start = (0, j)
print(start)

def print_lines(lines):
    print("\nCurrent state : ")
    for line in lines:
        print("".join(line))

splitters = 0
beams = [start]
print(len(lines), len(lines[0]))

for iteration in range(len(lines)-1):
    new_beams = []
    for beam in beams:
        print(beam)
        row, col = beam[0], beam[1]
        
        
        if lines[row + 1][col] == "^":
            splitters += 1
            new_beams.append((row + 1, col - 1))
            lines[row + 1][col - 1] = "|"

            new_beams.append((row + 1, col + 1))
            lines[row + 1][col + 1] = "|"

        else:
            new_beams.append((row + 1, col))
            lines[row + 1][col] = "|"
    
    print_lines(lines=lines)
    beams = set(new_beams)

print(splitters)