def calculate_savings_needed(ticket_price, start_month, end_month, monthly_expenses):
    # Assume 5k pocket money every month
    pocket_money = 5000

    total_months = end_month - start_month + 1

    total_expenses = total_months * monthly_expenses

    savings_needed = ticket_price - (total_months * pocket_money - total_expenses)

    return total_months, max(0, savings_needed)

def main():
    ticket_price = float(input("Enter the price of the flight ticket: "))

    monthly_expenses = float(input("Enter monthly expenses on necessities and luxury: "))

    start_month = int(input("Enter the start month of the semester: "))
    end_month = int(input("Enter the end month of the semester: "))
    total_months = end_month - start_month + 1
    total_months, savings_needed = calculate_savings_needed(ticket_price, start_month, end_month, monthly_expenses)
    if(savings_needed == 0):
      print("No need for additional savings you can just save ",ticket_price/total_months,"to make the cut") 
    else:
      print(f"Total months in the semester: {total_months}")
      print(f"Minimum amount Nisha must aditionally: {savings_needed:.2f}")

if __name__ == "__main__":
    main()
