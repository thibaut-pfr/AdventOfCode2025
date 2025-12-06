f = open("day5_input.txt")

#STORE IMPORTANT DATA
ranges = []

#DATA RETRIEVAL
i=0
lines = f.readlines()
while lines[i] != '\n':
        ranges.append(tuple(list(map(int, lines[i].strip().split("-")))))
        i += 1

#SORT BY RANGE STARTS
#print("Starting ranges : " + str(ranges))
ranges.sort(key=lambda x: x[0])
#print("Sorted ranges : " + str(ranges))

#ITERATE OVER RANGE TO CREATE NON-OVERLAPPING RANGES
final_ranges = []
cur_start = ranges[0][0]
cur_end = ranges[0][1]

for start,end in ranges[1:]:
        if start > cur_end:
                final_ranges.append((cur_start, cur_end))
                cur_start = start
                cur_end = end
        else :
                cur_end = max(cur_end,end)
final_ranges.append((cur_start,cur_end))

#print(final_ranges)

nr_valid = 0
for start,end in final_ranges:
        nr_valid += (end - start) + 1
        

print(nr_valid)