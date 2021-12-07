def rotate_90_degree_clckwise(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        li = list(map(lambda x: x[i], matrix))
        li.reverse()
        new_matrix.append(li)

    return new_matrix


def most_frequent(List):
    mf = max(set(List), key = List.count)
    result.append(mf)
    if mf == '0':
        result2.append('1')
    else:
        result2.append('0')            
 
def get_list():
    with open('day3\input3.txt','r') as f:
        input1=[]
        for line in f:
            strip_lines=line.strip()
            input1i=strip_lines.strip()
            input1.append(list(input1i))
            
    return input1

def binaryToDecimal(binary):
     
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

def convert_binary(s):
      
    # initialization of string to ""
    str1 = ""
    return binaryToDecimal((int(str1.join(s))))
      

result = []
result2 = []
input3 = rotate_90_degree_clckwise(get_list())


for i in range(0, len(input3)):
    most_frequent(input3[i])

print(convert_binary(result)*convert_binary(result2))

### PART 2 ####

input3 = get_list()


def purified_list(ls, value, pos):
    res = []
    for i in range(len(ls)):
        if ls[i][pos] == str(value):
            res.append(ls[i])
        
    return res
       

def life_support(list):
    result = []
    list_to_purify = list
    length= len(list[0])
    
    for i in range(length):
        common = 0 
        for u in range(len(list_to_purify )):
            if(list_to_purify[u][i]=='0'):
                common -= 1
            else:
                common += 1                
            
            #Si common es menor que 0, entonces 0 es el numero mas comun
            
            #Si comon es mayor o igual a 0, entonces 0 es el numero mas comun
            
            if common >= 0: # (<)
                to_append= '0'
            else:
                to_append= '1'
                
        list_to_purify = purified_list(list_to_purify,to_append,i)
    
        if (len(list_to_purify) == 1):
            result.append(convert_binary(list_to_purify[0]))
            
    return result
    
  


print(life_support(input3))