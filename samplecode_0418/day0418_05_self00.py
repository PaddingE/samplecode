str_test_string = "서울특별시 노원구 상계동 현대아파트"

print(len(str_test_string))
#길이 19 index는 0부터 18까지
print(str_test_string[3])
print(str_test_string[5])
print(str_test_string[18])


str_test_string1 = str_test_string[14] + str_test_string[2] + str_test_string[11]
print(str_test_string1)
print(str_test_string1[2])

str_test_string2 = (str_test_string1[0] * 8) + (str_test_string[18] * len(str_test_string1))
print(str_test_string2)

str_test_string3 = (str_test_string[5] * 3) + str_test_string2[:9]
print(str_test_string3)

print(str_test_string3[:5] + "\n" + str_test_string3[5:])