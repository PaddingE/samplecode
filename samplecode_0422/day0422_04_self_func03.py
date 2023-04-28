list_input = [1,2,[3,4],5,[6,7],[8,9]]
list_new = []

def list_flat(list_input):
    global list_new
    
    for i in list_input:
        if type(i) == list:
            list_flat(i)
            
        else:
            list_new.append(i)
            
list_flat(list_input)
            
print("""
{}를 평탄화하면
{}입니다.""".format(list_input, list_new))