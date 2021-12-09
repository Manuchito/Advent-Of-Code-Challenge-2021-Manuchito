def get_list():
    infile = open('day7\input7.txt', 'r')
    first_line = infile.readline()
    return first_line.strip().split(',')

def fuel2(place, dest):
    return sum([i for i in range(1, abs(place - dest) + 1)])

def fuel1(place, dest):
    return abs(place-dest)


crabs_pos = [int(x) for x in get_list()]

import statistics

part1_pos = [round(statistics.median(crabs_pos)) for i in range(max(crabs_pos))]
part1_fuel = sum(list(map(fuel1,crabs_pos, part1_pos)))

print(part1_fuel) # 328318


part2_pos = [int(sum(crabs_pos)/len(crabs_pos)) for i in range(max(crabs_pos))]
part2_fuel = sum(list(map(fuel2,crabs_pos, part2_pos)))

print(part2_fuel) # 89791146



    
