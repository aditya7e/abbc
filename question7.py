def calculate_total_score(math_marks, computer_marks, reasoning_marks, english_marks):
    return math_marks + computer_marks + reasoning_marks + english_marks

def generate_rank_card(students):
    ranked_students = sorted(students, key=lambda x: (x['total_score'], x['math_marks'], x['computer_marks'], x['reasoning_marks'], x['english_marks']), reverse=True)

    print("Rank Card:")
    print("{:<5} {:<10} {:<10} {:<5} {:<5} {:<5} {:<5} {:<5}".format("Rank", "Roll No", "Name", "Math", "Comp", "Reason", "English", "Total"))

    for rank, student in enumerate(ranked_students, start=1):
        print("{:<5} {:<10} {:<10} {:<5} {:<5} {:<5} {:<8} {:<5}".format(rank, student['rollnum'], student['name'], student['math_marks'], student['computer_marks'], student['reasoning_marks'], student['english_marks'], student['total_score']))

if __name__ == "__main__":
    num_students = int(input("Enter the total number of students: "))

    students = []
    for _ in range(num_students):
        rollnum = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        math_marks = int(input("Enter Math Marks: "))
        computer_marks = int(input("Enter Computer Marks: "))
        reasoning_marks = int(input("Enter Reasoning Marks: "))
        english_marks = int(input("Enter English Marks: "))

        total_score = calculate_total_score(math_marks, computer_marks, reasoning_marks, english_marks)

        student_data = {
            'rollnum': rollnum,
            'name': name,
            'math_marks': math_marks,
            'computer_marks': computer_marks,
            'reasoning_marks': reasoning_marks,
            'english_marks': english_marks,
            'total_score': total_score,
        }

        students.append(student_data)

    generate_rank_card(students)
