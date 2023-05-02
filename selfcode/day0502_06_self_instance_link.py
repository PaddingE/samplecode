class Student:
    def __init__(self):
        self.data = None
        self.link = None

def insert_student(name, score):
    global list_class, ptr_head, ptr_current, ptr_pre
    
    tuple_data = (name, score)
    
    c_student = Student()
    c_student.data = tuple_data
    list_class.append(c_student)
    
    if list_class == None:
        ptr_head = c_student
        return
    
    ptr_current = ptr_head
    
    while ptr_current.link != None:
        ptr_pre = ptr_current
        ptr_current = ptr_current.link
        
    ptr_current.link = c_student
        
def delete_student(name):
    global list_class, ptr_head, ptr_current, ptr_pre
    
    if ptr_head.data[0] == name:
        ptr_current = ptr_head
        ptr_head = ptr_head.link
        del(ptr_current)
        return
    
    ptr_current = ptr_head
        
    while ptr_current.link != None:
        ptr_pre = ptr_current
        ptr_current = ptr_current.link
        
        if ptr_current.data[0] == name:
            ptr_pre.link = ptr_current.link
            del(ptr_current)
            return
        
        
list_class = []
ptr_current, ptr_head, ptr_pre = None, None, None

if __name__ == "__main__":
    n_select = int(input("기능을 선택해 주세요(1.데이터 추가, 2. 데이터 삭제, 0. 종료): "))
    
    while n_select != 0:
        if n_select == 1:
            str_name = input("이름을 입력해 주세요: ")
            n_score = int(input("점수를 입력해 주세요: "))