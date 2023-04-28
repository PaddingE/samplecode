str_number = input("정수를 입력해주세요: ")
n_number = int(str_number)

for i in range(2,6):
    if n_number % i == 0:
        print("{}는 {}로 나누어 떨어지는 숫자입니다.".format(n_number, i))
    else:
        print("{}는 {}로 나누어 떨어지는 숫자가 아닙니다.".format(n_number, i))