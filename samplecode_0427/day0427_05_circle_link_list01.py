class Node():
    def __init__(self):
        self.data = None
        self.link = None
        
def print_nodes(start):
    current = start
    if current == None:
        return
    
    print(current.data, end = ' ')
    while current.link != start:
        current = current.link
        print(current.data, end = ' ')
        
    print()
    
list_memory = []
head, current, pre = None, None, None
list_data = ["다현", "정연", "쯔위", "사나", "지효"]

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