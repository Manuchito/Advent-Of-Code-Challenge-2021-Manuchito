def get_list():
    with open('day10\input10.txt','r') as f:
        input1=[]
        for line in f:
            strip_lines=line.strip()
            input1i=strip_lines.strip()
            input1.append(list(input1i))
            
    return input1

def convert_conector(value):
    if value == '[':
        return 2
    elif value == '(':
        return 1
    elif value == '{':
        return 3
    elif value == '<':
        return 4
    elif value == ']':
        return -2
    elif value == ')':
        return -1
    elif value == '}':
        return -3
    elif value == '>':
        return -4

def check_conec(matrix,score):
    for i in range(0,len(matrix)):
        expect =[]
        for u in range(0, len(matrix[i])):
            if matrix[i][u] > 0:
                expect.insert(0,matrix[i][u] * -1)
            else:
                if(matrix[i][u] == expect[0]):
                    expect.pop(0)
                else:
                    score[matrix[i][u]][1] += 1
                    break
    
conec = get_list()
score = {-2:[57,0], -1:[3,0], -3:[1197,0], -4:[25137,0]}
for i in range(0, len(conec)):
    conec[i] = list(map(convert_conector, conec[i]))


#check_conec(conec,score)
    
#result = 0
#for item in score:
#    result += score[item][1] * score[item][0]
    
#print(result) #392367


### PART 2 ###


def check_wrong_chunk(chunk):
    
    expect = []
    for u in range(0, len(chunk)):
        if chunk[u] > 0:
            expect.insert(0,chunk[u] * -1)
        else:
            if(chunk[u] == expect[0]):
                expect.pop(0)
            else:
                return False
            
    return True
              

purified_list = [x for x in conec if check_wrong_chunk(x)]

def correct_conec(matrix):
    res = []
 
    for i in range(0,len(matrix)):
        cnt = 0
        while True:
            
            if(cnt+1 == len(matrix[i])):
                break
            else:
                if(matrix[i][cnt] == matrix[i][cnt+1]*-1):
                    matrix[i].pop(cnt)
                    matrix[i].pop(cnt)
                    cnt-= 1
                else:
                    cnt += 1
                    
                    
        suma = 0             
        for i in reversed(matrix[i]):
            suma = suma * 5 + i
        res.append(suma)
        
    return sorted(res)[int(len(matrix)/2)]
                 
    

          
                
        

#print(correct_conec(purified_list)) #2192104158


    
