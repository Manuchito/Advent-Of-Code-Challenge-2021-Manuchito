def get_list():
    
    infile = open('day4\input4.txt', 'r')
    first_line = infile.readline()
    to_score = first_line.strip().split(',')
    
    with open('day4\input4.txt','r') as f:
        input1=[]
        matrix=[]
        for line in f:
            
            prov = line.strip().split()
            
            if(prov != []):
                matrix.append(prov)
                
            else:
                input1.append(matrix)
                matrix = []
                   
    return input1


### PART 1 ###          
def bingo(matrix):
    for y in range(len(matrix)):
        suma = 0
        #print(x,y)
        for x in range(len(matrix)):
            
            if matrix[x][y] == 'x':
                suma += 1
                if(suma == 5):
                    return True
            
            else:
                break
                suma = 0
        
        suma=0
        
        for x in range(len(matrix[0])):
            
            if matrix[y][x] == 'x':
                suma+=1
                if(suma == 5):
                    return True
                
            else:
                break
            
    return False

def cross_number(matrix, value):
    
    for y in range(len(matrix)):
        for x in range(len(matrix)):
            
            if matrix[x][y] == value:
                matrix[x][y] = 'x'
                
    return matrix
    
def solve(matrix, number_to_cross):
    for x in range(len(number_to_cross)):
        for i in range(len(matrix)):
            cross_number(matrix[i], number_to_cross[x])
        
            if(bingo(matrix[i])):
                print(matrix[i])
                res = get_values(matrix[i], number_to_cross[x])
                return(res)   

def get_values(used, mult):
    res = 0
    for x in range(len(used)):
        for y in range(len(used)):
            if used[x][y] != 'x':
                res += int(used[x][y])
            
    return res * int(mult)
                        
            
input4 = get_list()

number_to_cross = str(input4[0][0][0]).split(',')
bingos = input4[1:-1][:]



print(solve(bingos, number_to_cross))  #8442



        
### PART 2 ### 


def solve2(matrix, number_to_cross):
    res = []
    for x in range(len(number_to_cross)):
        for i in range(len(matrix)):
            cross_number(matrix[i], number_to_cross[x])
        
            if(bingo(matrix[i])):
                if i in res:
                    continue
                else:
                    res.append(i)
                    if len(res) == (len(matrix)):
                        print(matrix[i])
                        res = get_values(matrix[i], number_to_cross[x])
                        return(res)
                       
                    
   
            
print(solve2(bingos, number_to_cross))
