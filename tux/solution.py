def tux(numbers):

    if len(numbers) == 0:
        return -1
  
    index_min = numbers.index(min(numbers))
    index_max = numbers.index(max(numbers))  
    index_pivot = index_min + 1
  
    if index_max == len(numbers) - 1:
        return index_max
    if index_min == 0:
        return index_min
    if index_min > index_max:
        return -1
    for i in range(index_pivot):
        if numbers[index_pivot] <= numbers[i] and index_pivot != index_max:
            index_pivot += 1
            i = 0
        if numbers[index_pivot] <= numbers[i] and index_pivot == index_max - 1:
            return -1
    for i in range(index_pivot, len(numbers)):
        if numbers[index_pivot] > numbers[i]:
            return -1
        
    return index_pivot
  
