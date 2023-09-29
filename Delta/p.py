def calculate_grade(assignments, quizzes, midterm_exam, final_exam):
    if not (0 <= assignments <= 100) or not (0 <= quizzes <= 100) or not (0 <= midterm_exam <= 100) or not (0 <= final_exam <= 100):
        return "Invalid input scores. Scores must be between 0 and 100."
    total_weighted_score = (assignments * 0.25) + (quizzes * 0.20) + (midterm_exam * 0.25) + (final_exam * 0.30)
    if total_weighted_score >= 90:
        return "A"
    elif total_weighted_score >= 80:
        return "B"
    elif total_weighted_score >= 70:
        return "C"
    elif total_weighted_score >= 60:
        return "D"
    else:
        return "F"
print("--- Student Grade Calculator ---")
name = input("Enter Student Details:\nName: ")
roll_number = input("Roll Number: ")
age = input("Age: ")
assignments = float(input("Enter Course Components Scores:\nAssignments: "))
quizzes = float(input("Quizzes: "))
midterm_exam = float(input("Midterm Exam: "))
final_exam = float(input("Final Exam: "))
grade = calculate_grade(assignments, quizzes, midterm_exam, final_exam)
print("\n--- Result ---")
print("Name:", name)
print("Roll Number:", roll_number)
print("Age:", age)
print("Final Grade:", grade)