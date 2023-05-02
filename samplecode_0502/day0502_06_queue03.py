# queue에 데이터를 넣어주는 함수 선언
def enQueue(data):
    global SIZE, queue, front, rear
    
    if(rear == SIZE - 1):
        print("큐가 꽉 찼습니다.")
        return
    else:
        rear += 1
        queue[rear] = data

# queue의 데이터를 삭제하는 함수 선언        
def deQueue():
    global SIZE, queue, front, rear
    if(front == rear):
        print("큐가 비었습니다.")
        return None
    else:
        front += 1
        data = queue[front]
        queue[front] = None
        return data

# queue의 테이터를 삭제할때 빠저나갈 데이터를 알려주는 함수 선언
def peek():
    global SIZE, queue, front, rear
    
    if(front == rear):
        print("큐가 비었습니다.")
        return None
    else:
        return queue[front + 1]

# 전역변수 설정    
SIZE = int(input("큐 크기를 입력하세요 ==> "))
queue = [None for _ in range(SIZE)]
front = rear = -1

# 이 파일이 import되면 무시되는 부분
if __name__ == "__main__":
    select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")
    
    # select 값에 따라 함수 사용
    while(select != 'X' and select != 'x'):
        if select == 'I' or select == 'i':
            data = input("입력할 데이터 ==> ")
            enQueue(data)
            print("큐 상태: ", queue)
        elif select == 'E' or select == 'e':
            data = deQueue()
            print("추출된 데이터 ==> ", data)
            print("큐 상태: ", queue)
        elif select == 'V' or select == 'v':
            data = peek()
            print("확인된 데이터 ==> ", data)
            print("큐 상태: ", queue)
        else:
            print("입력이 잘못됨")
            
        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")
        
    print("프로그램 종료!")