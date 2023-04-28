str_input = input("염기 서열을 입력해주세요: ")
dict_codon = {}

for i in range(0, len(str_input),3):
    
    codon = str_input[i:i+3]
    
    if len(codon) == 3:
        if codon not in dict_codon:
            dict_codon[codon] = 0
        
        dict_codon[codon] += 1
    
print(dict_codon)