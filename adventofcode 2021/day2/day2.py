
def get_list():
    with open('day2\input2.txt','r') as f:
        input1=[]
        for line in f:
            strip_lines=line.strip()
            input1i=strip_lines.split()
            m=input1.append(input1i)
            
    return input1

depth=0
horizontal=0

commands = get_list()

for i in range(len(commands)):
    
    if(commands[i][0] == 'down'):
        depth += int(commands[i][1])
    elif(commands[i][0] == 'up'):
        depth -= int(commands[i][1])
    else:
        horizontal += int(commands[i][1])
        

print(horizontal*depth) # 1654760


### PART 2 ###

depth=0
horizontal=0
aim = 0
commands = get_list()

for i in range(len(commands)):
    
    if(commands[i][0] == 'down'):
        aim += int(commands[i][1])
    elif(commands[i][0] == 'up'):
        aim -= int(commands[i][1])
    else:
        intensity = int(commands[i][1])
        horizontal += intensity
        depth += intensity * aim
        

print(horizontal*depth) # 1956047400
