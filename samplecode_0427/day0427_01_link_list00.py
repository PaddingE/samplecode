class Node():
    def __init__(self):
        self.data = None
        self.link = None

# start노드 부터 끝 노드까지 데이터값 출력 해주는 함수        
def print_nodes(start):
    current = start
    
    # 저장된 노드가 없으면 함수 종료
    if current == None:
        return
    
    # 첫 노드 데이터 출력
    print(current.data, end = ' ')
    
    # 끝 노드 까지 데이터 출력
    while current.link != None:
        current = current.link
        print(current.data, end = ' ')
        
    print()

# 노드들의 데이터 값중에서 이름값들을 비교하여 작은값 순서로 노드 정리 해주는 함수    
def make_simple_linked_list(list_name_phone):
    global memory, head, current, pre
    
    print_nodes(head)
    
    # 노드에 데이터 저장후 메모리에 저장
    node = Node()
    node.data = list_name_phone
    memory.append(node)
    
    # head노드에 아무것도 없으면 생성한 노드를 head로 설정
    if head == None:
        head = node
        return
    
    # head노드 데이터의 이름값과 매개변수로 받은 데이터의 이름값을 비교해
    # 작으면 링크를 기존의 head노드로 연결하고, 생성한 노드를 head노드로 설정한다.
    if head.data[0] > list_name_phone[0]:
        node.link = head
        head = node
        return
    
    # 비교하려는 노드를 head노드로 초기화
    current = head
    
    # current노드가 끝 노드가 될때 까지 반복
    while current.link != None:
        pre = current
        current = current.link
        # current노드 데이터의 이름값과 매개변수로 받은 데이터의 이름값을 비교해서
        # current노드의 값이 더 크면 이전 노드의 링크를 생성한 노드로, 생성한 노드의
        # 링크를 current노드로 설정해 중간에 넣어준다.
        if current.data[0] > list_name_phone[0]:
            pre.link = node
            node.link = current
            return
    # 존재하는 노드들의 값보다 생성한 노드의 값이 크면 맨 뒤 노드로 설정한다.    
    current.link = node

# 전역변수 선언
memory = []
head, current, pre = None, None, None
list_of_list_data = [["지민", "010-1111-1111"], ["정국", "010-2222-2222"], ["뷔", "010-3333-3333"], 
                     ["슈가", "010-4444-4444"], ["진", "010-5555-5555"]]

# 이 파일이 import되면 무시되는 부분
if __name__ == "__main__":
    
    # list 안에 데이터 를 함수를 이용해 정리
    for data in list_of_list_data:
        make_simple_linked_list(data)
        
    print_nodes(head)