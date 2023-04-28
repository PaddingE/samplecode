# 리스트에 튜플 형태로 number가 큰 순서로 자료 넣는 함수
def add_data(name, number):
    list_kakao.append(None)
    n_len = len(list_kakao)
    
    # 리스트 뒤쪽부터 비교하면서 받은 값이 크면 기존값을 뒤로 미루고, 작으면 그자리에 저장
    for i in range(n_len - 1, 0, -1):
        if number < list_kakao[i - 1][1]:
            list_kakao[i] = (name, number)
            break
        else:
            list_kakao[i] = list_kakao[i - 1]
            list_kakao[i - 1] = (name, number)
    # 리스트가 아무것도 없는 상태에서 데이터를 넣는 경우        
    if n_len == 1:
        list_kakao[n_len -  1] == (name, number)

list_kakao = [("다현", 200), ("정연", 150), ("쯔위", 90), ("사나", 30), ("지효", 15)]

if __name__ == "__main__":
    str_name = input("저장할 이름을 입력하세요: ")
    n_number = int(input("문자 횟수를 입력하세요: "))
    
    add_data(str_name, n_number)
    
    print(list_kakao)

