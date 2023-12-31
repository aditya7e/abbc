def estimate_water_intake():
    print("Answer the following questions to estimate your daily water intake:")

    age = int(input("1. How old are you? "))
    weight = float(input("2. What is your weight in kilograms? "))
    activity_level = input("3. How would you describe your activity level? (sedentary/light/moderate/active): ").lower()

    # Estimate water intake based on general guidelines
    if activity_level == 'sedentary':
        estimated_intake = (weight / 30) * 1000  # 30 ml per kg
    elif activity_level == 'light':
        estimated_intake = (weight / 35) * 1000  # 35 ml per kg
    elif activity_level == 'moderate':
        estimated_intake = (weight / 40) * 1000  # 40 ml per kg
    elif activity_level == 'active':
        estimated_intake = (weight / 45) * 1000  # 45 ml per kg
    else:
        print("Invalid activity level. Assuming moderate activity.")
        estimated_intake = (weight / 40) * 1000

    return estimated_intake

daily_intake = int(input("Enter your daily intake of water(in ML): "))
remaining = estimate_water_intake()-daily_intake
if(remaining <= 0):
    print("You are Maintaing a healthy intake of water")
else:
    print("You require additional intake of:",remaining,"ML ")
