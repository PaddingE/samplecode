# %%
list_kakao2 = []
list_kakao2.append(None)
n_len_of_list = len(list_kakao2)
list_kakao2[n_len_of_list - 1] = "다현"
print(list_kakao2)
# %%
list_kakao2.append(None)
n_len_of_list = len(list_kakao2)
list_kakao2[n_len_of_list - 1] = "정연"
print(list_kakao2)
# %%
list_kakao3 = []

def add_data(name):
    list_kakao3.append(None)
    n_length = len(list_kakao3)
    list_kakao3[n_length - 1] = name
    
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')

print(list_kakao3)
# %%
list_kakao4 = ["다현", "정연", "쯔위", "사나", "지효"]

def insert_data(position, name):
    if position < 0 or position > len(list_kakao4):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return
    
    list_kakao4.append(None)
    n_leng2 = len(list_kakao4)
    
    for i in range(n_leng2 - 1, position, -1):
        list_kakao4[i] = list_kakao4[i-1]
        list_kakao4[i-1] = None
        
    list_kakao4[position] = name
    
insert_data(2, "솔라")
print(list_kakao4)
insert_data(6, "문별")
print(list_kakao4)
# %%
list_kakao5 = ["다현", "정연", "쯔위", "사나", "지효"]

def delete_data(position):
    if position < 0 or position > len(list_kakao4):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return
    
    n_len3 = len(list_kakao5)
    list_kakao5[position] = None
    
    for i in range(position + 1, n_len3):
        list_kakao5[i -1] = list_kakao5[i]
        list_kakao5[i] = None
        
    del(list_kakao5[n_len3 - 1])
    
delete_data(1)
print(list_kakao5)
delete_data(3)
print(list_kakao5)
# %%
