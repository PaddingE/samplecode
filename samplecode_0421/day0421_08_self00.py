list_numbers = [1,2,3,4,1,2,3,1,4,1,2,3]
dict_count = {}

for key in list_numbers:
    str_key = str(key)
    
    if str_key not in dict_count:
        dict_count[str_key] = 0
        
    dict_count[str_key] += 1
        
print("""{}에서
사용된 숫자의 종류는 {}개입니다.
참고: {}""".format(list_numbers, len(dict_count), dict_count))