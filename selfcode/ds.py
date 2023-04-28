# 필요한 함수를 쓰기 위해 random, math 모듈 사용
import random
import math

class Store():
    def __init__(self):
        self.data = None
        self.link = None

# 매개변수로 받은 start 노드부터 끝 노드까지 편의점 이름, 거리를 출력해주는 함수        
def print_store(start):
    current = start
    if current == None:
        return
    
    print(current.data[0],"거리 :", calcul_distance(current.data[1], current.data[2]))
    while current.link != start:
        
        current = current.link
        print(current.data[0],"거리 :", calcul_distance(current.data[1], current.data[2]))
        
    print()

# 거리 계산해주는 함수선언    
def calcul_distance(pos_x, pos_y):
    f_distance = math.sqrt(pos_x * pos_x + pos_y * pos_y)
    return f_distance

# 매개변수로 받은 데이터를 새로 만든 노드에 넣고
# 거리 비교후 알맞은 위치에 노드를 삽입해 주는 함수    
def data_insert(store_data):
    global list_store_data, head, current, pre
    
    store = Store()
    store.data = store_data
    list_store_data.append(store)
    
    # 노드가 없는 상태면 새로만든 노드를 head노드로 정한다.    
    if head == None:
        head = store
        store.link = head
        return     
    
    # 새로운 편의점과 head노드 편의점 거리를 계산
    f_store_distance = calcul_distance(store.data[1],store.data[2])
    f_head_distance = calcul_distance(head.data[1], head.data[2])
    
    # head노드 편의점 거리가 새로운 편의점 거리보다 멀면
    # 새로만든 노드 링크를 head로 연결하고, last로 끝 노드를
    # 찾은 다음 새로 만든 노드에 링크를 연결하고, 만든 노드를
    # head노드로 저장한다.  
    if f_head_distance > f_store_distance:
        store.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = store
        head = store
        return
            
    current = head
    
    # while 반복문으로 끝 노드 랑 비교할때 까지 current노드와
    # 만든 노드 거리 비교 후 중간에 노드 삽입 후 링크 조정
    while current.link != head:
        pre = current
        current = current.link
        f_current_distance = calcul_distance(current.data[1], current.data[2])
        if f_current_distance > f_store_distance:
            pre.link = store
            store.link = current
            return
    
    # 만든 노드가 가장긴 거리를 가지면 끝노드의 링크에
    # 만든 노드를 연결하고 만든 노드 링크에 head 저장           
    current.link = store
    store.link = head

# 전역변수 선언            
str_name = "A"
current, head, pre = None, None, None
list_store_data = []

# 이 파일이 import되면 무시하는 부분
if __name__ == "__main__":
    # random 함수를 이용해 store데이터를 튜플로 10개 만들어
    # data_insert 함수로 노드를 삽입한다.
    for i in range(1,11):
        store = (str_name + "편의점", random.randint(1,100), random.randint(1,100))
        data_insert(store)
        str_name = chr(ord(str_name) + 1)
        
    print_store(head)
        