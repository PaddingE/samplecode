str_number = input("정수를 입력해주세요: ")
n_number = int(str_number)
n_sum = 0
str_slice = ""

if n_number % 2 == 0:
    print("{}는 2로 나누어 떨어지는 숫자입니다.".format(n_number))
else:
    print("{}는 2로 나누어 떨어지는 숫자가 아닙니다.".format(n_number))
    
for i in str_number:
    n_sum += int(i)

if n_sum % 3 == 0:
    print("{}는 3로 나누어 떨어지는 숫자입니다.".format(n_number))
else:
    print("{}는 3로 나누어 떨어지는 숫자가 아닙니다.".format(n_number))
    
if len(str_number) <= 2:
    if n_number % 4 == 0:
        print("{}는 4로 나누어 떨어지는 숫자입니다.".format(n_number))
    else:
        print("{}는 4로 나누어 떨어지는 숫자가 아닙니다.".format(n_number))
else:
    str_slice = str_number[len(str_number) - 2] + str_number[len(str_number) - 1]
    n_slice_number = int(str_slice)
    if n_slice_number % 4 == 0:
        print("{}는 4로 나누어 떨어지는 숫자입니다.".format(n_number))
    else:
        print("{}는 4로 나누어 떨어지는 숫자가 아닙니다.".format(n_number))
        
if str_number[len(str_number) - 1] == 0 or str_number[len(str_number) - 1] == 5:
    print("{}는 5로 나누어 떨어지는 숫자입니다.".format(n_number))
else:
    print("{}는 5로 나누어 떨어지는 숫자가 아닙니다.".format(n_number))