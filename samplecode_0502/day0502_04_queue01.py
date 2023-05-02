# queue가 꽉 찼는지 확인해주는 함수
def is_queue_full():
    global SIZE, queue, front, rear
    
    # rear 포인터값이 SIZE - 1 이면 꽉 찬것으로 결정
    if(rear == SIZE - 1):
        return True
    else:
        return False

# data값을 매개변수로 받아서 queue에 넣어주는 함수    
def enQueue(data):
    global SIZE, queue, front, rear
    
    if (is_queue_full()):
        print("큐가 꽉 찼습니다.")
        return
    rear += 1
    queue[rear] = data

# 전역변수 설정
SIZE = 5
queue = ['화사', '솔라', '문별', '휘인', None]
front = -1
rear = 3

# 이 파일이 import되면 무시되는 부분
if __name__ == '__main__':
    
    # 함수 사용
    print(queue)
    enQueue('선미')
    print(queue)
    enQueue('재남')