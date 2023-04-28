list_numbers = [273,103,5,32,65,9,72,800,99]

for number in list_numbers:
    if number % 2 == 1:
        print(number, "는 홀수입니다.")
    else:
        print(number, "는 짝수입니다.")
        
for number in list_numbers:
    str_number = str(number)
    print(number, "는", len(str_number), "자릿수입니다.")