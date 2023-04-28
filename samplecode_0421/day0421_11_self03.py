list_input = [1,2,[3,4],5,[6,7],[8,9]]
list_new = []

for i in list_input:
    if type(i) == list:
        for j in i:
            list_new.append(j)
            
    else:
        list_new.append(i)
        
print("""
{}를 평탄화하면
{}입니다.""".format(list_input, list_new))