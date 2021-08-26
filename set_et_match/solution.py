def set_et_match(numbers, n):
    number_dict = dict.fromkeys(numbers)
    solutions = [num for num in numbers
                 if n - num in number_dict]
    return len(solutions) > 1
