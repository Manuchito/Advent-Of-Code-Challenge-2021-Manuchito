def get_list():
    with open('day5\input5.txt','r') as f:
        input1=[]
        for line in f:
            strip_lines=line.strip('\n')
            input1i=strip_lines.strip().split(' -> ')
            input1i=[x for xs in input1i for x in xs.split(',')]
            input1.append(list(input1i))
            
    return input1

def valids(coords):
    valids = []
    for i in range(len(coords)):
        if(coords[i][0]==coords[i][2]):
            valids.append(coords[i])
        elif(coords[i][1]==coords[i][3]):
            valids.append(coords[i])
            
    return valids

def to_mark(coords):
    mark=[]
    for u in range(len(coords)):
        
        x = [int(coords[u][0]),int(coords[u][2])]
        y = [int(coords[u][1]),int(coords[u][3])]
    
        if(x[0] == x[1]):
            for i in range(min(y),max(y)+1):
                mark.append((x[0],i))
                
        if(y[0] == y[1]):
            for i in range(min(x),max(x)+1):
                mark.append((i,y[0]))
        
    return mark
        
testing = get_list()
part_1 = valids(testing)  
marcas = to_mark(part_1)
marcas = sorted(marcas)

import collections
print(len([item for item, count in collections.Counter(marcas).items() if count > 1]))
#6113


        




















"""#####################################################################################################################################################################################################################################################################################################################################
        
lines = [i.replace("\n", "").split(" -> ") for i in open("day5/input5.txt", "r")]
conv = [[list(map(int, i[0].split(","))), list(map(int, i[1].split(",")))] for i in lines]
valids = []
wodiag = []

for i in conv:
    valids.append(i)
    if i[0][0] == i[1][0] or i[0][1] == i[1][1]:
        wodiag.append(i)

allpoints = [[], []]

for c in range(2):
    for i in (valids if c == 1 else wodiag):
        lh_x = [i[0][0], i[1][0]]
        lh_y = [i[0][1], i[1][1]]

        step_x = -1 if i[0][0] > i[1][0] else 1
        step_y = -1 if i[0][1] > i[1][1] else 1

        for x, y in zip(range(i[0][0], i[1][0] + step_x, step_x) if min(lh_x) != max(lh_x) else [min(lh_x)] * (max(lh_y) - min(lh_y) + 1), range(i[0][1], i[1][1] + step_y, step_y) if min(lh_y) != max(lh_y) else [min(lh_y)] * (max(lh_x) - min(lh_x) + 1)):
            allpoints[c].append([x, y])

h_x = int(max([i[j][0] for i in valids for j in range(2)])) + 1
h_y = int(max([i[j][1] for i in valids for j in range(2)])) + 1

current = [[[0 for i in range(h_x)] for j in range(h_y)] for a in range(2)]

for c in range(len(allpoints)):
    for i in range(len(allpoints[c])):
        current[c][allpoints[c][i][1]][allpoints[c][i][0]] += 1

print("at least 2 overlap without diags:", sum([j >= 2 for i in current[0] for j in i]))
print("at least 2 overlap with diags:", sum([j >= 2 for i in current[1] for j in i]))


#0,9 -> 5,9
#8,0 -> 0,8
#9,4 -> 3,4
"""

        


        
