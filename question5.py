def check_eligibility(academics, family_income, caste):
    academic_criteria = 80
    income_criteria = 50000
    caste_criteria = 'General'

    if academics >= academic_criteria and family_income < income_criteria and caste == caste_criteria:
        return True
    else:
        return False

def calculate_scholarship_amount(academics, family_income, caste):
    max_scholarship_amount = 5000
    loan_criteria = 3000

    if check_eligibility(academics, family_income, caste):
        return max_scholarship_amount
    else:
        return loan_criteria

def calculate_remaining_amount(scholarship_amount, total_tuition_fee):
    remaining_amount = total_tuition_fee - scholarship_amount
    return remaining_amount if remaining_amount > 0 else 0

def main():
    academics = float(input("Enter academic percentage: "))
    family_income = float(input("Enter family income: "))
    caste = input("Enter caste: ")

    total_tuition_fee = 10000

    scholarship_amount = calculate_scholarship_amount(academics, family_income, caste)
    remaining_amount = calculate_remaining_amount(scholarship_amount, total_tuition_fee)

    print(f"Scholarship amount: ${scholarship_amount}")
    print(f"Remaining amount to be paid: ${remaining_amount}")

if __name__ == "__main__":
    main()
