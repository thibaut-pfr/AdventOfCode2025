f = open("day5_input.txt")

#STORE IMPORTANT DATA
ranges = []
IDs = []

#DATA RETRIEVAL
i=0
lines = f.readlines()
while lines[i] != '\n':
        ranges.append(tuple(list(map(int, lines[i].strip().split("-")))))
        i += 1

for j in range(i+1, len(lines)):
        IDs.append(int(lines[j].strip()))

#SORT BY RANGE STARTS
print("Starting ranges : " + str(ranges))
ranges.sort(key=lambda x: x[0])
print("Sorted ranges : " + str(ranges))
print("IDs : " + str(IDs))

#ITERATE OVER RANGE TO CREATE NON-OVERLAPPING RANGES
final_ranges = []
cur_start = ranges[0][0]
cur_end = ranges[0][1]

for start,end in ranges[1:]:
        if start >= cur_end:
                final_ranges.append((cur_start, cur_end))
                cur_start = start
                cur_end = end
        else :
                cur_end = max(cur_end,end)
final_ranges.append((cur_start,cur_end))

print(final_ranges)
nr_valid = 0
for id in IDs:
        for start,end in final_ranges:
            if start <= id and id <= end:
                   nr_valid += 1
print(nr_valid)