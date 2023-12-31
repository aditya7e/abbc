import random

room_types = {
    "Standard": 1000,
    "Deluxe": 2000,
    "Suite": 3500,
}

def display_room_types():
    print("Room Types and Costs:")
    for room_type, cost in room_types.items():
        print(f"{room_type}: Rs.{cost} per night")

customer_name = input("Enter customer name: ")
customer_address = input("Enter customer address: ")

check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
check_out_date = input("Enter check-out date (YYYY-MM-DD): ")

num_nights = (int(check_out_date[8:]) - int(check_in_date[8:]))

display_room_types()

room_type = input("Enter the selected room type: ")

total_cost = room_types[room_type] * num_nights

bill_id = random.randint(1000, 9999)

print("\nFinal Bill:")
print(f"Bill ID: {bill_id}")
print(f"Customer Name: {customer_name}")
print(f"Customer Address: {customer_address}")
print(f"Room Type: {room_type}")
print(f"Check-In Date: {check_in_date}")
print(f"Check-Out Date: {check_out_date}")
print(f"Number of Nights: {num_nights}")
print(f"Total Cost: Rs.{total_cost}")

print("\nThank you for staying with us! We hope to see you again soon.")

