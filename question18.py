def calculate_bmr(gender, age, weight, height):
    if gender.lower() == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender.lower() == 'female':
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        raise ValueError("Invalid gender")

    return bmr

def calculate_tdee(bmr, heart_rate):
    if heart_rate < 60:
        activity_factor = 1.2
    elif 60 <= heart_rate < 100:
        activity_factor = 1.375
    elif 100 <= heart_rate < 120:
        activity_factor = 1.55
    else:
        activity_factor = 1.725

    tdee = bmr * activity_factor
    return tdee

gender = input("Enter gender (Male/Female): ")
age = int(input("Enter age: "))
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in cm: "))
heart_rate = int(input("Enter heart rate per minute: "))

bmr = calculate_bmr(gender, age, weight, height)
tdee = calculate_tdee(bmr, heart_rate)

print(f"\nBasal Metabolic Rate (BMR): {bmr:.2f} calories/day")
print(f"Total Daily Energy Expenditure (TDEE): {tdee:.2f} calories/day")

target_weight = float(input("\nEnter target body weight in kg: "))
calories_to_target = tdee + (target_weight - weight) * 7700
print(f"Calories needed to reach target weight: {calories_to_target:.2f} calories/day")
