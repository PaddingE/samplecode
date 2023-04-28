def calcul_sphere_vol(radius, CONST_PI = 3.141592):
    f_sphere_vol = 4 / 3 * CONST_PI * (radius ** 3)
    
    print("구의 부피는 {:.3f}입니다.".format(f_sphere_vol))
    
def calcul_sphere_surf(radius, CONST_PI = 3.141592):
    f_sphere_surf = 4 * CONST_PI * (radius ** 2)
    
    print("구의 겉넓이는 {:.3f}입니다.".format(f_sphere_surf))
    
f_input_radius = float(input("구의 반지름을 입력하세요> "))

calcul_sphere_vol(f_input_radius)
calcul_sphere_surf(f_input_radius)