def data_to_front():
    global SIZE, queue, front
    
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
    data_to_front()

SIZE = 5
queue = ['정국', '뷔', '지민', '진', '슈가']
front = -1
rear = 4

if __name__ == "__main__":
    
    print("대기줄 상태: ", queue)
    for i in range(len(queue)):
        deQueue()
        print("대기줄 상태: ", queue)
        
    print("식당 영업 종료!")