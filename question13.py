def calculate_marks(correct_answers, student_responses):
    marks = 0
    for question, correct_option in correct_answers.items():
        student_response = student_responses.get(question, "").upper()
        if student_response == correct_option:
            marks += 4
        elif student_response != "":
            marks -= 1
    return max(0, marks)

def main():
    correct_answers = {1: 'A', 2: 'B', 3: 'C', 4: 'D'}

    num_students = int(input("Enter the number of students: "))

    students_responses = {}

    for student_num in range(1, num_students + 1):
        print(f"\nStudent {student_num}'s responses:")
        student_responses = {}
        for question in range(1, 5):
            response = input(f"Question {question}: ").upper()
            student_responses[question] = response
        students_responses[student_num] = student_responses

    for student_num, responses in students_responses.items():
        marks = calculate_marks(correct_answers, responses)
        print(f"\nStudent {student_num}: Marks = {marks}")

if __name__ == "__main__":
    main()
