from D_Set.Models.subject import Subject
from D_Set.Models.student import Student
from D_Set.Models.grade import Grade
from datetime import date

student_id = 1
subject_id = 1
grade_id = 1
grade = 10
grade_date = "2024-12-22"
grade_date_1 = "2024-11-22"

onestudent = Student({
    "name": "John Doe",
    "age": 20,
    "email": "johnny.doe@example.com",
})

math = Subject({
    "name": "Mathematics",
})

Grade({
    "student_id": onestudent.get("id"),
    "subject_id": math.get("id"),
    "grade": grade,
})

Grade({
    "student_id": onestudent.get("id"),
    "subject_id": math.get("id"),
    "grade": grade-1,
    "grade_date": grade_date,
})

print(onestudent.get_grades())
print(onestudent.get_average_grade(math.get("id"), grade_date_1, date.today().isoformat()))
