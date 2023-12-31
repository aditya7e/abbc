def check_eligibility(age, weight, height, blood_pressure, last_donation_months):
    age_condition = 18 <= age <= 60
    weight_condition = 50 <= weight <= 150
    height_condition = 150 <= height <= 200
    blood_pressure_condition = blood_pressure <= 140
    last_donation_condition = last_donation_months >= 6

    return age_condition and weight_condition and height_condition and blood_pressure_condition and last_donation_condition

# Input user information
age = int(input("Enter age: "))
weight = float(input("Enter weight in kg: "))
height = int(input("Enter height in cm: "))
blood_pressure = int(input("Enter blood pressure (systolic): "))
last_donation_months = int(input("Enter months since the last blood donation: "))

# Overall eligibility
if check_eligibility(age, weight, height, blood_pressure, last_donation_months):
    print("You are eligible for blood donation!")
else:
    print("You are not eligible for blood donation based on the criteria.")
