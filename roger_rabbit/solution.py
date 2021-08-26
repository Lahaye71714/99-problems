def roger_rabbit(n):
    
    new_list = []
    
    for i in range (0, n + 1):
        if i == 1:
            new_list.append('1')
        if i > 1 and i % 2 == 0:
            new_list.append(new_list[(i // 2) - 1] + '0')
        if i > 1 and i % 2 == 1:
            new_list.append(new_list[(i // 2) - 1] + '1')
 
    return new_list
