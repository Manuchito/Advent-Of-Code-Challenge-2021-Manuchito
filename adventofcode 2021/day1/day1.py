import math

def get_list():
    with open('day1\input1.txt','r') as f:
        input1=[]
        for line in f:
            strip_lines=line.strip()
            m=input1.append(int(strip_lines))
            
    return input1

### PART 1 ###

def get_count_increased(input1):
    count = 0
    for i in range(1, len(input1)):
        if((input1[i]) > (input1[i-1])):
            count += 1
    
    print(count)

get_count_increased(get_list()) # 1624  
            

### PART 2 ###      
     
input1 = get_list()
count = 0
sums_l=[]
for i in range(0, int(math.floor(len(input1)/3)*3)):
    
    suma = 0
    for u in range(3): suma += input1[i+u]
    sums_l.append(suma)
    
    
get_count_increased(sums_l) # 1653