# 모듈 만들어서 사용하기

# test_module을 import 해서 test 라는 객체를 만듬
import test_module as test

# test 객체를 이용해 모듈 안에 있는 함수 사용
f_radius = test.number_input()
print(test.get_circumference(f_radius))
print(test.get_circle_area(f_radius))