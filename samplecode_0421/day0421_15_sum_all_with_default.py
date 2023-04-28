def sum_all(int_start = 0, int_end = 100, step = 1):
    int_output = 0
    
    for i in range(int_start, int_end + 1, step):
        int_output += i
        
    return int_output

print("A", sum_all(0,100,10))
print("B", sum_all(int_end=100))
print("C", sum_all(int_end=100, step=2))