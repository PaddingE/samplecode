def print_poly(p_x):
    term = len(p_x) - 1
    str_poly = "P(x) = "
    
    for i in range(len(p_x)):
        coef = p_x[i]
        
        if(coef >= 0):
            str_poly += "+"
        str_poly += str(coef) + "x^" + str(term) + " "
        term -= 1
        
    return str_poly

def calc_poly(xValue, p_x):
    retValue = 0
    term = len(p_x) - 1
    
    for i in range(len(p_x)):
        coef = p_x[i]
        retValue += coef * xValue ** term
        term -= 1
        
    return retValue


list_py = [7, -4, 0, 5]

if __name__ == "__main__":
    str_p = print_poly(list_py)
    print(str_p)
    
    xValue = int(input("X 값-->"))
    
    pxValue = calc_poly(xValue, list_py)
    print(pxValue)