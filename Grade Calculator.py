def marks_calculator():
    attendance = float(input("Enter attendance marks (out of 10): "))
    lab = float(input("Enter lab marks (out of 20): "))
    mid = float(input("Enter mid-term marks (out of 30): "))
    final = float(input("Enter final exam marks (out of 40): "))

    total_marks = attendance + lab + mid + final
    return total_marks


def grade_calculator(total_marks):
    percentage = (total_marks / 100) * 100  # Assuming total marks are out of 100
    if percentage <= 100 and percentage >= 80:
        return 'Your Point is 5.00 and Grade is A+'
    elif percentage < 79 and percentage >= 70:
        return 'Your Point is 4.00 and Grade is A'
    elif percentage < 69 and percentage >= 60:
        return 'Your Point is 3.50 and Grade is A-'
    elif percentage < 59 and percentage >= 50:
        return 'Your Point is 3.00 and Grade is B'
    elif percentage < 49 and percentage >= 40:
        return 'Your Point is 2.00 and Grade is C'
    elif percentage < 39 and percentage >= 33:
        return 'Your Point is 1.00 and Grade is D'
    else:
        return 'Your Point is 0.00 and Grade is F'



N = int(input("Enter the number of students: "))

for i in range(N):
    print(f"\nStudent {i + 1}:")

    total_marks = marks_calculator()

    grade = grade_calculator(total_marks)

    print(f"Total Marks: {total_marks}")
    print(f"Grade: {grade}")
