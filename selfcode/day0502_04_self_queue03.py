# queue 데이터를 앞으로 한칸씩 옮겨주는 함수
def go_front():
    global SIZE, queue, front
    
    # 반복문으로 뒤쪽에 있는 데이터를 앞으로 한칸 옮기고
    # 뒤 데이터를 None으로 만드는 부분
    for i in range(1,SIZE):
        if queue[i] == None:
            break
        
        queue[i -1] = queue[i]
        queue[i] = None
        
    front = -1
    

def deQueue():
    global SIZE, queue, front, rear
    
    if(front == rear):
        print("큐가 비어있습니다.")
        return

    print(queue[front + 1], "님 식당에 들어감")
    front += 1
    queue[front] = None
    go_front()
    
def enQueue(data):
    global SIZE, queue, rear
    
    if(rear == SIZE - 1):
        print("큐가 꽉 찼습니다.")
        return
    else:
        rear += 1
        queue[rear] = data

list_data = ['정국', '뷔', '지민', '진', '슈가']
SIZE = len(list_data)
queue = [None for _ in range(SIZE)]
front = -1
rear = -1

if __name__ == "__main__":
    
    for i in range(SIZE):
        enQueue(list_data[i])
    
    print("대기줄 상태: ", queue)
    for i in range(SIZE):
        deQueue()
        print("대기줄 상태: ", queue)
        
    print("식당 영업 종료!")