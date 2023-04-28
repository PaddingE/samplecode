def print_is_multiple(n_number, *n_multi_number):
    list_multi_num = [*n_multi_number]
    
    for n_multi_num in list_multi_num:
        if n_number % n_multi_num == 0:
            print("{}는 {}의 배수 입니다.".format(n_number, n_multi_num))
        else:
            print("{}는 {}의 배수가 아닙니다.".format(n_number, n_multi_num))


print_is_multiple(12, 2,3,4,5,6,12,11,7)