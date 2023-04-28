class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
class StudentList:
    def __init__(self):
        self.students = []
    
    # 객체의 students 리스트에 매개변수 값을 추가    
    def append_student(self, student):
        if type(student) == Student:
            self.students.append(student)
        else:
            print("매개변수의 타입이 Student가 아닙니다.")
    
    # 리스트 안에 Student 객체들의 점수 값들을 이용해서 평균 점수를 구하는 함수    
    def get_average(self):
        n_sum = 0
        for student in self.students:
            if type(student) == Student:
                n_sum += student.score
                
        f_avg = n_sum / len(self.students)
        
        return f_avg
    
    # 리스트 안에 Student 객체들의 점수 값들을 비교해 가장 높은 점수의 값을 가진 Student 객체를 리턴하는 함수
    def get_max_score(self):
        max_score_student = Student("", 0)
        
        for student in self.students:
            if type(student) == Student and student.score > max_score_student.score:
                max_score_student = student
                
        return max_score_student
    
    # 리스트 안에 Student 객체들의 점수 값들을 비교해 가장 낮은 점수의 값을 가진 Student 객체를 리턴하는 함수
    def get_min_score(self):
        min_score_student = Student("", 100)
        
        for student in self.students:
            if type(student) == Student and student.score < min_score_student.score:
                min_score_student = student
                
        return min_score_student


# 객체 생성후 데이터값 입력    
students = StudentList()
students.append_student(Student("구름", 100))
students.append_student(Student("별", 49))
students.append_student(Student("초코", 81))
students.append_student(Student("아지", 90))

# 객체로 함수와 데이터 사용
print(f"학급의 평균 점수는 {students.get_average()}입니다.")
print(f"가장 성적이 높은 학생은 {students.get_max_score().name}, 점수는 {students.get_max_score().score} 입니다.")
print(f"가장 성적이 높은 학생은 {students.get_min_score().name}, 점수는 {students.get_min_score().score} 입니다.")