CONST_PI = 3.141592

f_r = float(input("구의 반지름을 입력해주세요> "))

f_sphere_vol = 4 / 3 * CONST_PI * (f_r ** 3)
f_sphere_surf = 4 * CONST_PI * (f_r ** 2)

print("구의 부피는 {:.3f}입니다.".format(f_sphere_vol))
print("구의 겉넓이는 {:.3f}입니다.".format(f_sphere_surf))