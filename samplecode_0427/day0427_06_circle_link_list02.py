class Node():
    def __init__(self):
        self.data = None
        self.link = None

# start노드 부터 끝 노드까지 데이터값 출력 해주는 함수       
def print_nodes(start):
    current = start
    if current == None:
        return
    
    print(current.data, end = ' ')
    while current.link != start:
        current = current.link
        print(current.data, end = ' ')
        
    print()

# 찾는 데이터 앞에 원하는 데이터를 넣어주는 함수 선언    
def insert_node(findData, insertData):
    global list_memory, head, current, pre
    
    # 찾는 데이터가 head노드면 새 노드를 만들고 원하는 데이터를 넣는다.
    # 새로 만든 노드의 링크를 기존 head 노드 연결
    # last노드로 맨 끝 노드 링크를 새로 만든 노드로 연결하고
    # head노드를 만든 노드로 저장
    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return
    
    current = head
    # head노드로 링크한 노드까지 반복(중간 부분 노드 추가)
    while current.link != head:
        pre = current
        current = current.link
        # current노드의 데이터와 찾는 데이터 비교후 노드를 만들어 앞에 삽입
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
    # 찾는 데이터가 없으면 노드를 새로 만들어 데이터를 넣고
    # 끝 노드의 링크를 만든 노드로, 만든 노드의 링크를 head노드로 연결    
    node = Node()
    node.data = insertData
    current.link = node
    node.link = head

# 원하는 데이터를 가진 노드를 삭제해주는 함수 선언    
def delete_node(deleteData):
    global list_memory, head, current, pre
    
    # 지우려는 데이터가 head데이터면 
    if head.data == deleteData:
        current = head
        head = head.link
        last = head
        while last.link != current:
            last = last.link
        
        last.link = head
        del(current)
        return
    
    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return
        
# 전역 변수 선언    
list_memory = []
head, current, pre = None, None, None
list_data = ["다현", "정연", "쯔위", "사나", "지효"]

# 이 파일이 import되면 무시되는 부분
if __name__ == "__main__":
    node = Node()
    node.data = list_data[0]
    head = node
    node.link = head
    list_memory.append(node)
    
    for data in list_data[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        list_memory.append(node)
        
    print_nodes(head)
    
    insert_node("다현", "화사")
    print_nodes(head)
    
    insert_node("사나", "솔라")
    print_nodes(head)
    
    insert_node("재남", "문별")
    print_nodes(head)
    
    delete_node("화사")
    print_nodes(head)
    
    delete_node("정연")
    print_nodes(head)
    
    delete_node("문별")
    print_nodes(head)