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
    
def insert_node(findData, insertData):
    global memory, head, current, pre
    
    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return
    
    current = head
    while current.link != None:
        pre = current
        current = current.link
        
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
        
    node = Node()
    node.data = insertData
    current.link = node
    
def delete_node(deletedata):
    global memory, head, current, pre
    
    if head.data == deletedata:
        current = head
        head = head.link
        del(current)
        print("#첫 노드가 삭제됨#")
        return
    
    current = head
    
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deletedata:
            pre.link = current.link
            del(current)
            print("#중간 노드가 삭제됨#")
            return
    print("#삭제된 노드가 없음#")

def find_node(find_data):
    global memory, head, current, pre
    
    current = head
    if current.data == find_data:
        return current
    
    while current.link != None:
        current = current.link
        if current.data == find_data:
            return current
    return Node()

memory = []
head, current, pre = None, None, None
list_data = ["다현", "정연", "쯔위", "사나", "지효"]

if __name__ == "__main__":
    
    node = Node()
    node.data = list_data[0]
    head = node
    memory.append(node)
    
    for data in list_data[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)
        
    print_nodes(head)
        
    insert_node("다현", "화사")
    print_nodes(head)
    
    insert_node("사나", "솔라")
    print_nodes(head)
    
    insert_node("재남", "문별")
    print_nodes(head)
    
    delete_node("화사")
    print_nodes(head)
    
    delete_node("쯔위")
    print_nodes(head)
    
    delete_node("지현")
    print_nodes(head)
    
    f_node = find_node("다현")
    print(f_node.data)
    f_node = find_node("사나")
    print(f_node.data)
    f_node = find_node("지현")
    print(f_node.data)