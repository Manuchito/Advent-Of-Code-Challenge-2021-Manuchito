from os import pipe


test = [['1', '0', '0', '1', '0', '0', '0', '0', '1', '0', '1', '1'],
        ['0', '0', '0', '0', '1', '0', '0', '1', '0', '1', '0', '1'],
        ['0', '1', '1', '1', '0', '0', '1', '0', '0', '0', '0', '1'],
        ['0', '1', '1', '1', '0', '0', '1', '0', '0', '0', '0', '1'],
        ['0', '1', '0', '1', '0', '0', '0', '0', '1', '0', '1', '1'],
        ['0', '1', '0', '0', '1', '0', '0', '1', '0', '1', '0', '1'],
        ['0', '1', '0', '0', '1', '1', '0', '1', '1', '0', '0', '1'],
        ['0', '1', '1', '0', '0', '0', '1', '0', '0', '1', '1', '1'], 
        ['0', '1', '0', '0', '0', '0', '1', '1', '1', '0', '1', '1'],
        ['0', '1', '0', '1', '1', '0', '0', '0', '1', '0', '0', '1'], 
        ['0', '1', '1', '1', '1', '1', '0', '1', '0', '1', '1', '1'],
        ['0', '1', '0', '1', '1', '0', '0', '1', '1', '0', '1', '0'],
        ['0', '1', '0', '0', '1', '0', '1', '0', '0', '0', '1', '1'], 
        ['0', '1', '1', '0', '0', '1', '1', '1', '1', '0', '1', '0'], 
        ['0', '1', '1', '1', '0', '0', '0', '0', '1', '1', '1', '0']]

#0 0 0 1 / 0 0 0 0 / 0 0 0 1

def purified_list(ls, value, pos):
    res = []
    for i in range(len(ls)):
        if ls[i][pos] == str(value):
            res.append(ls[i])
        
    return res
       

result = []

def life_support(lista):
    result = []
    list_to_purify = lista
    length = len(list_to_purify[0])
    
    for i in range(length):
        common = 0 
        for u in range(len(list_to_purify)):
            if(list_to_purify[u][i]=='0'):
                common -= 1
            else:
                common += 1                
            
        if(common<0):
            to_append = '0'
        else:
           to_append ='1'
        
        list_to_purify=purified_list(list_to_purify,to_append,i)
        print(list_to_purify)
     
        
life_support(test)               


    
#0 0 0 0 / 0 1 0 1 / 1 0 1 1            
[['0', '1', '0', '1', '0', '0', '0', '0', '1', '0', '1', '1'],
 ['0', '1', '0', '0', '1', '0', '0', '1', '0', '1', '0', '1'],
 ['0', '1', '0', '0', '1', '1', '0', '1', '1', '0', '0', '1'],
 ['0', '1', '1', '0', '0', '0', '1', '0', '0', '1', '1', '1'], 
 ['0', '1', '0', '0', '0', '0', '1', '1', '1', '0', '1', '1'],
 ['0', '1', '0', '1', '1', '0', '0', '0', '1', '0', '0', '1'], 
 ['0', '1', '1', '1', '1', '1', '0', '1', '0', '1', '1', '1'],
 ['0', '1', '0', '1', '1', '0', '0', '1', '1', '0', '1', '0'],
 ['0', '1', '0', '0', '1', '0', '1', '0', '0', '0', '1', '1'], 
 ['0', '1', '1', '0', '0', '1', '1', '1', '1', '0', '1', '0'], 
 ['0', '1', '1', '1', '0', '0', '0', '0', '1', '1', '1', '0']]