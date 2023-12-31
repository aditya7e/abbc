def display_atm_state(atm_state):
    print("ATM State:")
    for denomination, count in atm_state.items():
        print(f"{denomination} notes: {count}")

def withdraw_money(atm_state, amount):
    withdrawn_notes = {}
    
    for denomination in sorted(atm_state.keys(), reverse=True):
        if amount >= denomination and atm_state[denomination] > 0:
            num_notes = amount // denomination
            withdrawn_notes[denomination] = num_notes
            amount -= num_notes * denomination
            atm_state[denomination] -= num_notes
    
    if amount == 0:
        print("Withdrawal successful! Notes withdrawn:")
        for denomination, count in withdrawn_notes.items():
            print(f"{count} notes of {denomination}")
    else:
        print("Sorry, unable to withdraw the requested amount. Please try a different amount.")

# Initial ATM state
atm_state = {2000: 10, 500: 20, 200: 30, 100: 50, 50: 100, 20: 200, 10: 300, 5: 500, 2: 1000, 1: 2000}

while True:
    display_atm_state(atm_state)
    amount_to_withdraw = int(input("Enter the amount you want to withdraw (or 'exit' to quit): "))

    if amount_to_withdraw == 'exit':
        print("Exiting the program. Thank you!")
        break

    withdraw_money(atm_state, amount_to_withdraw)
