str_input = input("염기 서열을 입력해주세요: ")
dict_count = {"a": 0, "t": 0, "g": 0, "c": 0}

for key in str_input:
    dict_count[key] += 1
    
print("""
a의 개수: {}
t의 개수: {}
g의 개수: {}
c의 개수: {}""".format(dict_count["a"], dict_count["t"], dict_count["g"], dict_count["c"]))