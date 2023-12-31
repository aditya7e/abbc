
def find_faulty_subswitch(short_circuited_houses):
    sub_switches = {1: [1, 2, 3, 4, 5],
                   2: [6, 7, 8, 9, 10],
                   3: [11, 12, 13, 14, 15]}

    for sub_switch, houses in sub_switches.items():
        if all(house in short_circuited_houses for house in houses):
            return "Cut supply from Main switch"

        if any(house in short_circuited_houses for house in houses):
            return f"Cut supply from Sub-switch {sub_switch}"

    return "No action needed"

def main():
    short_circuited_houses = set(map(int, input("Enter the houses experiencing a short circuit (comma-separated): ").split(',')))

    result = find_faulty_subswitch(short_circuited_houses)
    print(result)

if __name__ == "__main__":
    main()
