# 초기 설정
queue = ['화사', '솔라', '문별', None, None]
front = -1
rear = 2

# queue에 들어있는 값 출력
print("--------큐 상태--------")
print('[출구]<-- ', end=' ')

for i in range(0, len(queue), 1):
    print(queue[i], end=' ')
    
print('<-- [입구]')
print("-----------------------")

# front 포인터로 앞에 있는 데이터부터 제거하고 None으로 초기화
front += 1
data = queue[front]
queue[front] = None
print('deQueue -->', data)

front += 1
data = queue[front]
queue[front] = None
print('deQueue -->', data)

front += 1
data = queue[front]
queue[front] = None
print('deQueue -->', data)
print("-----------------------")

# queue에 들어있는 값 출력
print("--------큐 상태--------")
print('[출구]<-- ', end=' ')

for i in range(0, len(queue), 1):
    print(queue[i], end=' ')
    
print('<-- [입구]')