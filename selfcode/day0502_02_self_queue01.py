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

SIZE = 5
queue = ['화사', None, None, None, None]
front = -1
rear = 0

if __name__ == "__main__":
    print(queue)
    ret_data = deQueue()
    print("추출한 데이터 -->", ret_data)
    print(queue)
    ret_data = deQueue()