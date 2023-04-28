def sum_all(int_start, int_end):
    int_sum = 0
    
    for i in range(int_start, int_end +1):
        int_sum += i
        
    return int_sum

print("0 to 100:", sum_all(0,100))
print("0 to 1000:", sum_all(0,1000))
print("50 to 100:", sum_all(50,100))
print("500 to 1000:", sum_all(500,1000))