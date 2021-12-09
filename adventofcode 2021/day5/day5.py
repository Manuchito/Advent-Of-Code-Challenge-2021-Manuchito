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
                
        elif(y[0] == y[1]):
            for i in range(min(x),max(x)+1):
                mark.append((i,y[0]))
        
        else:
            m = (y[0] - y[1]) / (x[0] - x[1]);
            c = y[0] - x[0] * m;
    
            for i in range(min(x), max(x)+1):
                x_res = i
                y_res = int(i*m + c, )
                mark.append((x_res,y_res))
        
    return mark
        
testing = get_list()

part_1 = sorted(to_mark(valids(testing)))

import collections

print(len([item for item, count in collections.Counter(part_1).items() if count > 1])) #6113

### PART 2 ###

part_2 = sorted(to_mark(testing))
print(len([item for item, count in collections.Counter(part_2).items() if count > 1])) #20373