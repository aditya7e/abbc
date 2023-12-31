# Dictionary containing information about chemical elements
chemical_elements = {
    'hydrogen': {'atomic_number': 1, 'atomic_mass': 1.008, 'symbol': 'H', 'fact': 'The lightest and most abundant element in the universe.'},
    'helium': {'atomic_number': 2, 'atomic_mass': 4.0026, 'symbol': 'He', 'fact': 'It was first discovered in the Sun before it was found on Earth.'},
    'carbon': {'atomic_number': 6, 'atomic_mass': 12.011, 'symbol': 'C', 'fact': 'The basis for organic chemistry and life on Earth.'},
    'oxygen': {'atomic_number': 8, 'atomic_mass': 15.999, 'symbol': 'O', 'fact': 'Essential for respiration in living organisms.'},
    'gold': {'atomic_number': 79, 'atomic_mass': 196.967, 'symbol': 'Au', 'fact': 'Highly valued for its rarity and use in jewelry.'},
}

def display_element_info(element_name):
    element_name = element_name.lower()
    if element_name in chemical_elements:
        element_info = chemical_elements[element_name]
        print(f"\nElement: {element_name.capitalize()}")
        print(f"Atomic Number: {element_info['atomic_number']}")
        print(f"Atomic Mass: {element_info['atomic_mass']}")
        print(f"Symbol: {element_info['symbol']}")
        print(f"Fact: {element_info['fact']}")
    else:
        print(f"\nElement '{element_name}' not found in the database.")

def add_fact(element_name, new_fact):
    element_name = element_name.lower()
    if element_name in chemical_elements:
        chemical_elements[element_name]['fact'] = new_fact
        print(f"\nNew fact added for {element_name.capitalize()}: {new_fact}")
    else:
        print(f"\nElement '{element_name}' not found in the database.")

def main():
    while True:
        print("\nChemical Element Information Program")
        print("1. Display Element Information")
        print("2. Add Fact about an Element")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            element_name = input("\nEnter the name of the element: ")
            display_element_info(element_name)
        elif choice == '2':
            element_name = input("\nEnter the name of the element: ")
            new_fact = input("Enter a new fact about the element: ")
            add_fact(element_name, new_fact)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
