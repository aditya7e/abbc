def extract_date_components(date_str):
    # Extract day, month, and year from the date string without using split
    day = int(date_str[0:2])
    month = int(date_str[3:5])
    year = int(date_str[6:])
    return day, month, year

def calculate_library_fine(expected_date, actual_date):
    exp_day, exp_month, exp_year = extract_date_components(expected_date)
    act_day, act_month, act_year = extract_date_components(actual_date)

    if act_year < exp_year or (act_year == exp_year and act_month < exp_month):
        return 500
    elif act_year == exp_year and act_month == exp_month and act_day <= exp_day:
        return 0
    elif act_year == exp_year and act_month == exp_month:
        return 5 * (act_day - exp_day)
    elif act_year == exp_year:
        return 50 * (act_month - exp_month)

# Example usage
expected_return_date = input("Enter the expected return date (dd:mm:yyyy): ")
actual_return_date = input("Enter the actual return date (dd:mm:yyyy): ")

fine = calculate_library_fine(expected_return_date, actual_return_date)
print("Fine:", fine, "RS")
