import random

# Dictionary to map fuel types to numerical values
fuel_types = {"Petrol": "01", "Diesel": "02", "CNG": "03"}

def generate_vehicle_number(state, city, fuel_type, vehicle_type, year_of_registration):
    # Use the first two letters of the state name as the state code
    state_code = state[:2].upper()

    # Get the numerical value for the fuel type from the dictionary
    fuel_code = fuel_types.get(fuel_type, "00")

    # Randomly generate a 2-digit unique number
    unique_number = random.randint(1, 99)

    # Constructing the simplified vehicle number
    vehicle_number = f"{state_code}{fuel_code}{city[:2].upper()}{vehicle_type[0].upper()}{year_of_registration[-2:]}{unique_number}"

    return vehicle_number

def main():
    state = input("Enter the state (e.g., Delhi, Maharashtra, Tamil Nadu): ")
    city = input("Enter the city: ")
    fuel_type = input("Enter the fuel type (e.g., Petrol, Diesel, CNG): ")
    vehicle_type = input("Enter the vehicle type (e.g., LMV, MCWG): ")
    year_of_registration = input("Enter the year of registration (YYYY): ")

    vehicle_number = generate_vehicle_number(state, city, fuel_type, vehicle_type, year_of_registration)

    if vehicle_number:
        print(f"Generated Vehicle Number: {vehicle_number}")

if __name__ == "__main__":
    main()
