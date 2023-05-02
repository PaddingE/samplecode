# 원형 queue에 데이터가 꽉찼는지 알려주는 함수
def is_queue_full():
    global SIZE, front, rear
    # front 포인터가 어디에 있든지 rear포인터의 값 + 1 값을 queue 사이즈로 나누고
    # 나온 값이 front 포인터의 값과 같으면 queue가 꽉 차있다는 뜻
    if((rear+1)%SIZE == front):
        return True
    else:
        return False

# 원형 queue에 데이터가 비어있는지 알려주는 함수    
def is_queue_empty():
    global SIZE, front, rear
    
    # front 포인터와 rear 포인터의 값이 같으면 비어있다는 뜻
    if(front == rear):
        return True
    else:
        return False

# 데이터를 매개변수로 받아 queue에 추가하는 함수    
def enQueue(data):
    global SIZE, queue, front, rear
     
    if (is_queue_full()):
        print("큐가 꽉 찼습니다.")
        return
    # 원형 queue이기 때문에 rear 포인터 설정시 값을 계산후 설정
    rear = (rear + 1) % SIZE
    queue[rear] = data

# queue의 맨 앞 데이터를 제거하는 함수    
def deQueue():
    global SIZE, queue, front
    
    if(is_queue_empty()):
        print("큐가 비었습니다.")
        return None
    
    # 원형 queue이기 때문에 front 포인터 설정시 값을 계산후 설정
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

# 데이터 제거시 제거되는 데이터를 확인시켜주는 함수
def peek():
    global SIZE, queue, front, rear
    
    if(is_queue_empty()):
        print("큐가 비었습니다.")
        return None
    else:
        # 원형 queue이기 때문에 front 포인터 설정시 값을 계산후 설정
        return queue[(front + 1) % SIZE]

# 전역변수 설정
SIZE = int(input("큐 크기를 입력하세요 ==> "))
queue = [None for _ in range(SIZE)]
front = rear = 0

# 이 파일이 import 되면 무시되는 부분
if __name__ == "__main__":
    select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")
    
    # select 값에 따라 함수 사용
    while(select != 'X' and select != 'x'):
        if select == 'I' or select == 'i':
            data = input("입력할 데이터 ==> ")
            enQueue(data)
            print("큐 상태: ", queue)
            print("front : ", front, ", rear : ", rear)
        elif select == 'E' or select == 'e':
            data = deQueue()
            print("추출된 데이터 ==> ", data)
            print("큐 상태: ", queue)
            print("front : ", front, ", rear : ", rear)
        elif select == 'V' or select == 'v':
            data = peek()
            print("확인된 데이터 ==> ", data)
            print("큐 상태: ", queue)
            print("front : ", front, ", rear : ", rear)
        else:
            print("입력이 잘못됨")
            
        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")
        
    print("프로그램 종료!")