def calculate_iq_score(total_score):
    if total_score <= 10:
        return "Below Average"
    elif total_score <= 20:
        return "Average"
    elif total_score <= 30:
        return "Above Average"
    else:
        return "High"

def take_iq_test():
    questions = [
        {"question": "1. What is 2 + 2?", "options": ["a. 3", "b. 4", "c. 5", "d. 6"], "correct_answer": "b"},
        {"question": "2. Which planet is known as the Red Planet?", "options": ["a. Earth", "b. Mars", "c. Jupiter", "d. Venus"], "correct_answer": "b"},
        {"question": "3. What is the capital of France?", "options": ["a. Paris", "b. Rome", "c. Berlin", "d. Madrid"], "correct_answer": "a"},
    ]

    total_score = 0

    for question in questions:
        print(question["question"])
        for option in question["options"]:
            print(option)
        answer = input("Your answer: ").lower()

        if answer == question["correct_answer"]:
            total_score += 1

    iq_score = calculate_iq_score(total_score)
    print(f"\nYour IQ Score: {iq_score}")

if __name__ == "__main__":
    print("Welcome to the IQ Test!")
    take_iq_test()
