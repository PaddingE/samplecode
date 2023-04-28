CONST_PI = 3.141592

def number_input():
    str_output = input("숫자 입력> ")
    return float(str_output)

def get_circumference(radius):
    return 2 * CONST_PI * radius

def get_circle_area(radius):
    return CONST_PI * radius * radius

#import 당할 때는 사용 되지 않는 구문
if __name__ == "__main__":
    print("get_circumference(10):", get_circumference(10))
    print("get_circle_area(10):", get_circle_area(10))