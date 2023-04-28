# class를 이용한 객체 생성
class Student:
    
    count = 0
    
    # __init__ 생성자 함수는 class 객체를 생성하면 무조건 처음 실행하는 함수
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        
        # class변수 count로 객체가 몇개 생성 되었는지 세는 부분
        Student.count += 1
        print("{}번째 학생이 생성되었습니다.".format(Student.count))
        
    def get_sum(self):
        return self.korean + self.english + self.math + self.science
    
    def get_average(self):
        return self.get_sum() / 4
    
    def to_string(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())

#         instances
student1 = Student("윤인성", 87, 98, 88, 95)
student2 = Student("연하진", 92, 98, 96, 98)

# class를 dictionary 형식으로 정리해서 출력
print(Student.__dict__)

# instances를 dictionary 형식으로 정리해서 출력
print(student1.__dict__)
print(student2.__dict__)

print("name\tsum\tavg")

print(student1.to_string())
print(student2.to_string())

# instance의 타입이 Student클래스가 맞는지 확인하는 구문
print(isinstance(student1,Student))