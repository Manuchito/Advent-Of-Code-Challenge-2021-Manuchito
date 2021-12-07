coord = [[1,1,2,3]]



def getCount(coords):
    mark = []
    x = [int(coords[0][0]), int(coords[0][2])]
    y = [int(coords[0][1]),int(coords[0][3])]
    
    m = (y[0] - y[1]) / (x[0] - x[1]);
    c = y[0] - x[0] * m;
    
    for i in range(min(x), max(x)+1):
        x_res = i
        y_res = int(i*m + c, )
        mark.append((x_res,y_res))
        
    return mark
        
    
    
print(getCount(coord))