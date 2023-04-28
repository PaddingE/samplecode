def print_poly(t_x, p_x):
    str_poly = "P(x) = "
    
    for i in range(len(p_x)):
        term = t_x[i]
        coef = p_x[i]
        
        if(coef >= 0):
            str_poly += "+"
        str_poly += str(coef) + "x^" + str(term) + " "
        
    return str_poly

def calc_poly(xVal, t_x,  p_x):
    retValue = 0
    
    for i in range(len(p_x)):
        term = t_x[i]
        coef = p_x[i]
        retValue += coef * xVal ** term
        
    return retValue

list_ty = [300, 20, 0]
list_py = [7, -4, 5]

if __name__ == "__main__":
    str_p = print_poly(list_ty, list_py)
    print(str_p)
    
    xValue = int(input("X 값-->"))
    
    pxValue = calc_poly(xValue, list_ty, list_py)
    print(pxValue)