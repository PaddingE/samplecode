def calcul_hypo(n_base, n_height):    
    f_hypo = (n_base ** 2 + n_height ** 2) ** (1/2)
    
    print("빗변의 길이는 {}입니다.".format(f_hypo))
    
f_base = float(input("밑변의 길이를 입력해주세요: "))
f_height = float(input("높이의 길이를 입력해주세요: "))

calcul_hypo(f_base, f_height)