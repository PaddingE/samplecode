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
    # stack이 꽉차있는 경우에 return함
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
        print("스택이 비어있습니다.")
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

# stack의 top에 있는 내용을 리턴 해주는 함수
def peek():
    global SIZE, stack, top
    
    # stack이 비어있으면 None을 return 한다.
    if (is_stack_empty()):
        print("스택이 비었습니다.")
        return None
    
    return stack[top]

# 필요한 전역변수 선언    
SIZE = int(input("스택 크기를 입력하세요 ==> "))
stack = [None for _ in range(SIZE)]
top = -1

# 이 파일이 import 되면 무시되는 부분
if __name__ == "__main__":
    select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")
    
    # 입력 받은 내용에 따라 함수 사용
    while (select != 'X' and select != 'x'):
        if select == 'I' or select == 'i':
            data = input("입력할 데이터 ==> ")
            push(data)
            print("스택 상태: ", stack)
        elif select == 'E' or select == 'e':
            data = pop()
            print("추출된 데이터 ==> ", data)
            print("스택 상태: ", stack)
        elif select == 'V' or select == 'v':
            data = peek()
            print("확인된 데이터 ==> ", data)
            print("스택 상태: ", stack)
        else:
            print("입력이 잘못됨")
            
        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")
    
    print("프로그램 종료!")