def count_num(list_numbers):
    dict_count = {}
    
    for number in list_numbers:
        str_number = str(number)
    
        if str_number not in dict_count:
            dict_count[str_number] = 0
        
        dict_count[str_number] += 1
        
    print(dict_count)

list_numbers = [1,2,3,4,1,2,3,1,4,1,2,3]

count_num(list_numbers)