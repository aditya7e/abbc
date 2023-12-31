class Passenger:
    def __init__(self, name, age, weight, gender, medical_complications):
        self.name = name
        self.age = age
        self.weight = weight
        self.gender = gender
        self.medical_complications = medical_complications

def allocate_seats(passengers):
    senior_citizens = []
    specially_abled = []
    children = []
    women = []
    men = []

    for passenger in passengers:
        if passenger.age >= 60:
            senior_citizens.append(passenger)
        elif passenger.medical_complications == "Yes":
            specially_abled.append(passenger)
        elif passenger.age < 18:
            children.append(passenger)
        elif passenger.gender == "Female":
            women.append(passenger)
        else:
            men.append(passenger)

    allocated_seats = senior_citizens + specially_abled + children + women + men

    return allocated_seats

def main():
    num_passengers = int(input("Enter the number of passengers: "))
    passengers = []

    for i in range(num_passengers):
        print(f"\nEnter details for passenger #{i + 1}:")
        name = input("Name: ")
        age = int(input("Age: "))
        weight = float(input("Weight: "))
        gender = input("Gender (Male/Female): ").capitalize()
        medical_complications = input("Medical Complications (Yes/No): ").capitalize()

        passenger = Passenger(name, age, weight, gender, medical_complications)
        passengers.append(passenger)

    allocated_seats = allocate_seats(passengers)

    print("\nSeat allocation:")
    for i, passenger in enumerate(allocated_seats, start=1):
        print(f"Seat #{i}: {passenger.name}")

if __name__ == "__main__":
    main()
