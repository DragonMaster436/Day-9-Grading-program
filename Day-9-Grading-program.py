student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.

student_grades = {}


# TODO-2: Write your code below to add the grades to student_grades.👇

score_rank = {
    "high": "Outstanding",
    "medium": "Exceeds Expectations",
    "low": "Acceptable",
    "bad": "Fail"
}

# run a for loop and every time add them to the new dictionary with the scores using if statment
for key in student_scores:

    student_grades[key] = student_scores[key]

    if student_scores[key] > 90:
        student_grades[key] = score_rank["high"]

    elif student_scores[key] > 80:
        student_grades[key] = score_rank["medium"]

    elif student_grades[key] > 70:
        student_grades[key] = score_rank['low']
        
    elif student_grades[key] <= 70:
        student_grades[key] = score_rank["bad"]


# 🚨 Don't change the code below 👇
print(student_grades)