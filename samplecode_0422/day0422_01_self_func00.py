import datetime

def print_string(str_input):
    
    time_now = datetime.datetime.now()
    
    if "안녕" in str_input:
        print("안녕하세요.")
    elif "몇 시" in str_input:
        print("지금은 {}시 입니다.".format(time_now.hour))
    else:
        print(str_input)

str_input = input("입력: ")

print_string(str_input)