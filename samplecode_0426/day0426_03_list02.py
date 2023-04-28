# 리스트에 새로운 이름을 저장하는 함수 선언
def add_data(name):
    # 리스트에 빈 정보를 끝에 만들고
    # 그 빈 곳에 매개변수로 넣은 값을 저장
    list_kakao.append(None)
    n_len = len(list_kakao)
    list_kakao[n_len - 1] = name
    
# 원하는 위치에 이름을 저장하는 함수 선언
def insert_data(position, name):
    # 저장 위치가 올바른지 확인
    if position < 0 or position > len(list_kakao):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return
    # 저장 전 끝에 빈 정보 만들기
    list_kakao.append(None)
    n_len = len(list_kakao)
    
    # for 반복문으로 뒤에서부터 원하는 위치까지 빈 정보를 앞으로 당긴다.
    for i in range(n_len - 1, position, -1):
        list_kakao[i] = list_kakao[i-1]
        list_kakao[i-1] = None
        
    # 원하는 위치에 저장하기
    list_kakao[position] = name
    
# 원하는 위치의 데이터를 제가하는 함수 선언
def delete_data(position):
    # 위치가 올바른지 확인
    if position < 0 or position > len(list_kakao):
        print("데이터를 제거할 범위를 벗어났습니다.")
        return
    
    # 원하는 위치의 정보 빈칸으로 만들기
    n_len = len(list_kakao)
    list_kakao[position] = None
    
    # for 반복문으로 빈 정보 뒤로 미루기
    for i in range(position + 1, n_len):
        list_kakao[i -1] = list_kakao[i]
        list_kakao[i] = None
        
    # 빈 정보 지우기
    del(list_kakao[n_len - 1])
    
list_kakao = []
select = -1

# 이 파일이 import되면 무시하는 부분
if __name__ == "__main__":
    
    while(select!=4):
        
        select = int(input("선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)-->"))
        
        if(select == 1):
            data = input("추가할 데이터--> ")
            add_data(data)
            print(list_kakao)
        elif(select == 2):
            pos = int(input("삽입할 위치-->" ))
            data = input("추가할 데이터--> ")
            insert_data(pos, data)
            print(list_kakao)
        elif(select == 3):
            pos = int(input("삭제할 위치--> "))
            delete_data(pos)
            print(list_kakao)
        elif(select == 4):
            print(list_kakao)
            exit
        else:
            print("1~4중 하나를 입력하세요.")
            continue