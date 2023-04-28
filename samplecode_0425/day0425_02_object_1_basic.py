# 객체를 list에 직접 타이핑 해서 for반복 문으로 사용한는 프로그램

# list안에 dictionary값을 직접 넣는다.
list_students = [
    { "name": "윤인성", "korean": 87, "math": 98, "english": 88, "science": 95 },
    { "name": "연하진", "korean": 92, "math": 98, "english": 96, "science": 98 },
    { "name": "구지연", "korean": 76, "math": 96, "english": 94, "science": 90 },
    { "name": "나선주", "korean": 98, "math": 92, "english": 96, "science": 92 },
    { "name": "윤아린", "korean": 95, "math": 98, "english": 98, "science": 98 },
    { "name": "윤명월", "korean": 64, "math": 88, "english": 92, "science": 92 }
]

print("이름", "총점", "평균", sep="\t")

# for 반복문으로 list 안에있는 객체들의 정보를 이용해 값을 출력
for student in list_students:
    score_sum = student["korean"] + student["math"] + student["english"] + student["science"]
    score_average = score_sum / 4
    
    print(student["name"], score_sum, score_average, sep="\t")