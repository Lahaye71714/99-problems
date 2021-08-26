def morning_sunshine(numbers):
        new_list = []
        j = 0
        
        if len(numbers) < 2:
                return numbers
        elif len(numbers) > 1:
                new_list.append(numbers[len(numbers) -1])
                for i in numbers[::-1]:
                        if i > new_list[j]:
                                new_list.append(i)
                                j += 1
                new_list.reverse()

        return new_list
