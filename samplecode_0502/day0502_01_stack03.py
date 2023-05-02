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
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

# 괄호 열고 닫는 순서가 맞는지 확인해주는 함수 선언
def check_bracket(expr):
    for ch in expr:
        # 여는 괄호면 스택에 삽입
        if ch in '([{<':
            push(ch)
        
        # 닫는 괄호면 스택에서 빠짐    
        elif ch in ')]}>':
            out = pop()
            # 검색된 문자와 스택에서 빠지는 문자가 같은 닫는 괄호가 아니면 
            if ch == ')' and out == '(':
                pass
            elif ch == ']' and out == '[':
                pass
            elif ch == '}' and out == '{':
                pass
            elif ch == '>' and out == '<':
                pass
            else:
                return False
        else:
            pass
    if is_stack_empty():
        return True
    else:
        return False

# 전역변수 설정
SIZE = 100
stack = [None for _ in range(SIZE)]
top = -1

# 이 파일이 import되면 무시하는 부분
if __name__ == "__main__":
    
    exprAry = ['(A+B)', ')A+B()', '((A+B)-C', '(A+B]', '(<A+{B-C}/[C*D]>)']
    
    # 함수 사용
    for expr in exprAry:
        top = -1
        print(expr,'==>',check_bracket(expr))