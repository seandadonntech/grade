student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
student_grades = {}

for student in student_scores:
 print(student)
score = student_scores[student]
if score > 90:
 student_grades[student] = "outstanding"
elif score > 80:
 student_grades[student] = "exceeds expectation"
elif score > 70:
 student_grades[student] = "ACCEPTABLE"
else:
 student_grades[student] = "you failed"
print(student_grades)
