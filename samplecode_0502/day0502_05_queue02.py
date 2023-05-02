# queue가 비었는지 확인해주는 함수
def is_queue_empty():
    global SIZE, queue, front, rear
    
    # front 포인터와 rear 포인터의 값이 같으면 queue가 비어있다고 판단
    if(front == rear):
        return True
    else:
        return False

# queue의 앞에서 부터 데이터 값을 제거해주는 함수    
def deQueue():
    global SIZE, queue, front, rear
    # queue가 비어있는지 확인
    if(is_queue_empty()):
        print("큐가 비었습니다.")
        return None
    
    # queue가 비어있지 않으면 제일 앞의 데이터를 None으로 초기화하고,
    # 지운 데이터값을 return 해준다.
    front += 1
    data = queue[front]
    queue[front] = None
    return data

# 전역변수 설정
SIZE = 5
queue = ['화사', None, None, None, None]
front = -1
rear = 0

# 이 파일이 import되면 무시하는 부분
if __name__ == "__main__":
    # 함수 사용
    print(queue)
    ret_data = deQueue()
    print("추출한 데이터 -->", ret_data)
    print(queue)
    ret_data = deQueue()