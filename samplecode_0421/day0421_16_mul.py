def mul(*values):
    mul_number = 1
    
    for num in values:
        mul_number *= num
        
    return mul_number

print(mul(5,7,9,10))