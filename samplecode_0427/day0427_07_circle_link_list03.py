import random

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
    
def count_odd_even():
    global list_memory,head, current, pre
    
    counter_odd = 0
    counter_even = 0
    
    if head == None:
        return False
    
    current = head
    
    while True:
        if current.data % 2 == 0:
            counter_even += 1
        else:
            counter_odd += 1
        
        if current.link == head:
            break
        
        current = current.link
        
    return counter_even, counter_odd

def make_zero_number(even, odd):
    if even > odd:
        n_reminder = 0
    else:
        n_reminder = 1
        
    current = head
    
    while True:
        if current.data % 2 == n_reminder:
            current.data *= -1
        if current.link == head:
            break
        current = current.link

list_memory = []
head, current, pre = None, None, None

if __name__ == "__main__":
    
    list_data = []
    for _ in range(7):
        list_data.append(random.randint(1,100))
        
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
    
    n_counter_even, n_counter_odd = count_odd_even()
    
    print('홀수-->', n_counter_odd, '\t', '짝수-->', n_counter_even)
    
    
    make_zero_number(n_counter_even, n_counter_odd)
    
    print_nodes(head)