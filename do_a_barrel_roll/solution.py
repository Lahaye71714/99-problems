def do_a_barrel_roll(numbers, k):

        if k == 0 or numbers == []:
                return numbers

        if k > len(numbers):
                while k > len(numbers):
                        k = k - len(numbers)

        if k == len(numbers):
                return numbers
        
        if k < len(numbers):
                list1 = [x for x in range(0, k)]
                list2 = [x for x in range(k, len(numbers))]
                list2.extend(list1)
                return list2
