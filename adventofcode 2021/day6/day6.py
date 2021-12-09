def get_list():
    with open('day6\input6.txt','r') as f:
        input1=[]
        for line in f:
            strip_lines=line.split(',')
            return list(map(int, strip_lines))
            
def solve(fishes_dic, days):  
    
    for x in range(days):
        new_dic = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
        
        for i in range(0,8):
            if(fishes_dic[0] > 0):
            
                new_dic[8] = fishes_dic[0]
                new_dic[6] = fishes_dic[7] + fishes_dic[0]
                
            new_dic[i] = fishes_dic[i+1] 
            
        fishes_dic = new_dic    
       
    return fishes_dic


input_day6 = get_list()
input_day6 = {x:input_day6.count(x) for x in input_day6}

for i in range(0,9):
    if i not in input_day6:
        input_day6[i] = 0
    

print("Part 1:", sum(solve(input_day6, 80).values())) #362740


print("Part 2:",sum(solve(input_day6, 256).values())) # 1644874076764



"""for i in range(256):
    
    eggs = fishes.count(0)
    if eggs > 0:
        for i in range(eggs):
            fishes.append(9)
        
    fishes = [6 if fish == 0 else fish-1 for fish in fishes]
    print(len(fishes))"""
  
  

