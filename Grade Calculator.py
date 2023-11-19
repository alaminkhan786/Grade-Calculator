def marks_calculator():
    attendance = float(input("Enter attendance marks (out of 10): "))
    lab = float(input("Enter lab marks (out of 20): "))
    mid = float(input("Enter mid-term marks (out of 30): "))
    final = float(input("Enter final exam marks (out of 40): "))

    total_marks = attendance + lab + mid + final
    return total_marks


def grade_calculator(total_marks):
    percentage = (total_marks / 100) * 100  # Assuming total marks are out of 100
    if percentage >= 90:
        return 'A'
    elif 80 <= percentage < 90:
        return 'B'
    elif 70 <= percentage < 80:
        return 'C'
    elif 60 <= percentage < 70:
        return 'D'
    else:
        return 'F'



N = int(input("Enter the number of students: "))

for i in range(N):
    print(f"\nStudent {i + 1}:")

    total_marks = marks_calculator()

    grade = grade_calculator(total_marks)

    print(f"Total Marks: {total_marks}")
    print(f"Grade: {grade}")
