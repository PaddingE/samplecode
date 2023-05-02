# 데이터를 매개변수로 받아 queue에 넣어주는 함수
def enQueue(data):
    global SIZE, queue, rear
    
    if(rear == SIZE - 1):
        print("대기줄이 꽉 찼습니다.")
        return
    else:
        rear += 1
        queue[rear] = data

# queue 데이터를 앞으로 한칸씩 옮겨주는 함수        
def go_front():
    global SIZE, queue, front, rear
    
    # 반복문으로 뒤쪽에 있는 데이터를 앞으로 한칸 옮기고
    # 뒤 데이터를 None으로 만드는 부분
    for i in range(1,SIZE):
        if queue[i] == None:
            break
        
        queue[i - 1] = queue[i]
        queue[i] = None
    # queue 데이터를 앞으로 옮기고 front 포인터와 rear 포인터를 다시 초기화    
    front = -1
    rear -= 1
    
# queue의 제일 앞 데이터를 제거해주는 함수
def deQueue():
    global queue, front, rear
    
    if(front == rear):
        print("대기줄이 비어있습니다.")
        return

    # 제일 앞 데이터를 지우고 go_front 함수 사용
    front += 1
    data = queue[front]
    queue[front] = None
    go_front()
    return data

# 전역변수 설정
SIZE = 5
queue = [None for _ in range(SIZE)]
front = -1
rear = -1

# 이 파일이 import되면 무시되는 함수
if __name__ == "__main__":
    select = input("대기 추가(I)/입장(E)/종료(X) 중 하나를 선택 ==> ")
    
    # select 값에 따라 함수 사용
    while(select != 'X' and select != 'x'):
        if select == 'I' or select == 'i':
            data = input("대기손님 이름 ==> ")
            enQueue(data)
            print("대기손님 현황: ", queue)
        elif select == 'E' or select == 'e':
            data = deQueue()
            print("입장 손님 ==> ", data)
            print("대기손님 현황: ", queue)
        else:
            print("입력이 잘못됨")
            
        select = input("대기 추가(I)/입장(E)/종료(X) 중 하나를 선택 ==> ")
        
    print("식당 영업 종료!")