class Node():
    def __init__(self):
        self.data = None
        self.link = None
        
def print_nodes(start):
    current = start
    if current == None:
        return
    
    print(current.data, end = ' ')
    while current.link != None:
        current = current.link
        print(current.data, end = ' ')
        
    print()
    
def data_insert(name, e_mail):
    global list_memory, head, current, pre
    
    node = Node()
    node.data = [name, e_mail]
    list_memory.append(node)
    
    if head == None:
        head = node
        return
    
    if head.data[1] > node.data[1]:
        node.link = head
        head = node
        return
    
    current = head
    
    while current.link != None:
        pre = current
        current = current.link
        if current.data[1] > node.data[1]:
            pre.link = node
            node.link = current
            return
        
    current.link = node
    
def data_input():
    str_name = input("이름을 입력해 주세요: ")
    if str_name == "":
        return 0
    str_e_mail = input("이메일을 입력해 주세요: ")
    
    data_insert(str_name, str_e_mail)
    
    return 1
    
def delete_node(deletedata):
    global list_memory, head, current, pre
    
    if head.data[0] == deletedata:
        current = head
        head = head.link
        del(current)
        print("#첫 노드가 삭제됨#")
        return
    
    current = head
    
    while current.link != None:
        pre = current
        current = current.link
        if current.data[0] == deletedata:
            pre.link = current.link
            del(current)
            print("#중간 노드가 삭제됨#")
            return
    print("#삭제된 노드가 없음#")

list_memory = []
head, current, pre = None, None, None
select = -1

if __name__ == "__main__":
    while select != 0:
        select = int(input("기능을 선택해 주세요(1.데이터 추가, 2. 데이터 삭제, 0. 종료): "))
        
        if select == 1:
            select = data_input()
            
            print_nodes(head)
            
        elif select == 2:
            str_name = input("삭제할 이름을 입력하세요: ")
            
            delete_node(str_name)
            print_nodes(head)
            
        else:
            print_nodes(head)