# stack이 다 차 있는지 확인해주는 함수
def is_stack_full():
    global SIZE, stack, top
    if(top >= SIZE - 1):
        return True
    else:
        return False

# stack이 비어있는지 확인해주는 함수    
def is_stack_empty():
    global SIZE, stack, top
    if (top == -1):
        return True
    else:
        return False

# 매개변수 데이터를 stack에 추가해주는 함수
def push(data):
    global SIZE, stack, top
    
    if (is_stack_full()):
        print("스택이 꽉 찼습니다.")
        return
    top += 1
    stack[top] = data

# stack 데이터의 top에 있는 데이터를 제거해 None으로 해주는 함수    
def pop():
    global SIZE, stack, top
    
    # stack이 비어있으면 None을 return
    if(is_stack_empty()):
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

# 데이터 값 list를 매개변수로 받아 stack에 넣고 출력해주는 함수 
def string_to_snack(list_color):
    global stack
    str_print = '과자집에 가는길 : '
    # 데이터 값들을 stack에 push 해주고 push된 값들을 string값으로 저장
    for color in list_color:
        push(color)
        str_print += (stack[top] + '-->')
        
    str_print += '과자집'
    
    # 저장된 string값 return
    return str_print

# stack에 있는 데이터들을 꺼내면서 출력해주는 함수
def string_to_home():
    global SIZE, stack
    str_print = '우리집에 오는길 : '
    # stack에서 데이터 값들을 pop해주고, pop된 값들을 string값으로 저장
    for i in range(SIZE):
        str_print += (stack[top] + '-->')
        pop()
        
    str_print += '우리집'
    
    # 저장된 string값 return
    return str_print

# 전역변수 설정
top = -1
list_color = ['주황', '초록', '파랑', '보라', '빨강', '노랑']
SIZE = len(list_color)
stack = [None for _ in range(SIZE)]

# 이 파일이 import되면 무시하는 부분
if __name__ == "__main__":
    # 함수 사용
    print(string_to_snack(list_color))
    print(string_to_home())