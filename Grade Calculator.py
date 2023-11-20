def marks_calculator(attendance, lav, mid_term, final):
    total_marks = attendance + lav + mid_term + final

    if attendance <= 10 and attendance >= 0:
        if lav <= 20 and lav >= 0:
            if mid_term <= 30 and mid_term >= 0:
                if final <= 40 and final >= 0:
                    return total_marks
                else:
                    print('Invalid Marks!\nPlease Try again later.')
            else:
                print('Invalid Marks!\nPlease Try again later.')
        else:
            print('Invalid Marks!\nPlease Try again later.')
    else:
        print('Invalid Marks!\nPlease Try again later.')


def grade_calculator(total_marks):
    if total_marks <= 100 and total_marks >= 80:
        return 'Your Grade is A+'
    elif total_marks <= 79 and total_marks >= 70:
        return 'Your Grade is A'
    elif total_marks <= 69 and total_marks >= 60:
        return 'Your Grade is A-'
    elif total_marks <= 59 and total_marks >= 50:
        return 'Your Grade is B'
    elif total_marks <= 49 and total_marks >= 40:
        return 'Your Grade is C'
    elif total_marks <= 39 and total_marks >= 33:
        return 'Your Grade is D'
    elif total_marks <= 32 and total_marks >= 0:
        return 'Your Grade is F'
    else:
        print('Invalid Marks!\nPlease Try again later.')


N = int(input("Enter the total number: "))

for i in range(N):
    print(f"\nStudent: {i + 1}")

    attendance = float(input("Enter your Attendance marks: "))
    lav = float(input("Enter your Lav marks: "))
    mid_term = float(input("Enter your Mid-Term exam marks: "))
    final = float(input("Enter your Final exam marks: "))
    total_marks = marks_calculator(attendance, lav, mid_term, final)
    if total_marks is not None:
        grade = grade_calculator(total_marks)
        
        print("total marks:", total_marks)
        print("Grade:", grade)