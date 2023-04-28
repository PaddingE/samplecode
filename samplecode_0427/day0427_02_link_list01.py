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
    while current.link != None:
        current = current.link
        print(current.data, end = ' ')
        
    print()

# 매개변수 이름과 이메일을 받아서 노드를 저장하는 함수 선언    
def data_insert(name, e_mail):
    global list_memory, head, current, pre
    
    # 노드를 새로 만들어 매개변수로 받은 데이터를 넣고 메모리에 저장
    node = Node()
    node.data = [name, e_mail]
    list_memory.append(node)
    
    # 저장된 노드가 없으면 새로 만든 노드를 헤드노드로 저장
    if head == None:
        head = node
        return
    
    # head노드 데이터의 이메일 값과 생성한 노드 데이터의 이메일 값을 비교하여
    # head노드 값이 크면 새로 만든 노드의 링크를 기존의 head노드로 연결하고,
    # 새로 만든 노드를 head로 저장한다.
    if head.data[1] > node.data[1]:
        node.link = head
        head = node
        return
    
    current = head
    
    # current노드가 끝 노드가 될때 까지 반복
    while current.link != None:
        pre = current
        current = current.link
        # current노드 데이터의 이메일 값과 매개변수로 받은 데이터의 이메일 값을 비교해서
        # current노드의 값이 더 크면 이전 노드의 링크를 생성한 노드로, 생성한 노드의
        # 링크를 current노드로 설정해 중간에 넣어준다.
        if current.data[1] > node.data[1]:
            pre.link = node
            node.link = current
            return
        
    current.link = node

# 원하는 데이터를 가진 노드를 삭제해 주는 함수 선언    
def delete_node(deletedata):
    global list_memory, head, current, pre
    
    # head데이터의 이름이 지우려는 데이터면 head노드를
    # 다음 노드로 저장하고, current노드를 삭제
    if head.data[0] == deletedata:
        current = head
        head = head.link
        del(current)
        print("#첫 노드가 삭제됨#")
        return
    
    current = head
    
    # current노드가 끝 노드가 될때 까지 반복 
    while current.link != None:
        pre = current
        current = current.link
        # current노드 데이터의 이름값과 삭제하려는 데이터가 같으면
        # 이전 노드의 링크를 current노드 링크에 저장하고,
        # current노드 삭제
        if current.data[0] == deletedata:
            pre.link = current.link
            del(current)
            print("#중간 노드가 삭제됨#")
            return
    print("#삭제된 노드가 없음#")

# 전역변수 선언
list_memory = []
head, current, pre = None, None, None
select = -1

# 이 파일을 import 하면 무시되는 부분
if __name__ == "__main__":
    # select 값이 0 이면 프로그램 종료
    while select != 0:
        select = int(input("기능을 선택해 주세요(1.데이터 추가, 2. 데이터 삭제, 0. 종료): "))
        
        # 데이터 추가 입력시 이름을 입력할 때 enter를 누르면 select를 0으로 저장하고
        # 다음 반복을 진행하는데 진행시 select 값이 0이라 프로그램 종료
        if select == 1:
            str_name = input("이름을 입력해 주세요: ")
            if str_name == '':
                select = 0
                continue
            
            str_e_mail = input("이메일을 입력해 주세요: ")
            
            data_insert(str_name, str_e_mail)
            
            print_nodes(head)
            
        elif select == 2:
            str_name = input("삭제할 이름을 입력하세요: ")
            
            delete_node(str_name)
            print_nodes(head)
            
        else:
            print_nodes(head)
        
        