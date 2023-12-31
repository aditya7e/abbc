flights = {
    "Flight1": {"time_taken": 5, "ticket_cost": 200, "seats_available": 50},
    "Flight2": {"time_taken": 4, "ticket_cost": 150, "seats_available": 30},
    "Flight3": {"time_taken": 6, "ticket_cost": 180, "seats_available": 40},
    "Flight4": {"time_taken": 3, "ticket_cost": 120, "seats_available": 60},
    "Flight5": {"time_taken": 7, "ticket_cost": 220, "seats_available": 35},
    "Flight6": {"time_taken": 4, "ticket_cost": 160, "seats_available": 45},
}

def min_ticket_cost_flight(flight_data):
    min_cost_flight = min(flight_data, key=get_ticket_cost)
    return min_cost_flight, flight_data[min_cost_flight]["ticket_cost"]

def min_time_taken_flight(flight_data):
    min_time_flight = min(flight_data, key=get_time_taken)
    return min_time_flight, flight_data[min_time_flight]["time_taken"]

def average_ticket_cost(flight_data):
    total_cost = sum(data["ticket_cost"] for data in flight_data.values())
    num_flights = len(flight_data)
    return total_cost / num_flights if num_flights > 0 else 0

def highest_cost_per_hour(flight_data):
    cost_per_hour = {flight: flight_data[flight]["ticket_cost"] / flight_data[flight]["time_taken"] for flight in flight_data}
    max_cost_flight = max(cost_per_hour, key=cost_per_hour.get)
    return max_cost_flight, cost_per_hour[max_cost_flight]

def get_ticket_cost(flight):
    return flight_data[flight]["ticket_cost"]

def get_time_taken(flight):
    return flight_data[flight]["time_taken"]

min_cost_flight, min_ticket_price = min_ticket_cost_flight(flights)
print(f"Minimum Ticket Cost: {min_ticket_price} (Flight: {min_cost_flight})")

min_time_flight, min_duration = min_time_taken_flight(flights)
print(f"Minimum Time Taken: {min_duration} hours (Flight: {min_time_flight})")

avg_ticket_cost = average_ticket_cost(flights)
print(f"Average Ticket Cost: {avg_ticket_cost}")

max_cost_hour_flight, max_cost_per_hour = highest_cost_per_hour(flights)
print(f"Highest Cost Per Hour: {max_cost_per_hour} (Flight: {max_cost_hour_flight})")
