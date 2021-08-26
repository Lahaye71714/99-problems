def daemon(numbers, k):
    x = 0
 
    while x < k:
        if numbers[x] >= numbers[k]:
            return(False)
        else:
            x += 1

    if x == k:
        x += 1

    while x < len(numbers):
        if numbers[x] < numbers[k]:
            return(False)
        else:
            x += 1
            
    return(True)
