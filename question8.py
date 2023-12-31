def identify_country_and_validate(number, country_codes):
    prefix = number[:2]

    if prefix in country_codes:
        country = country_codes[prefix]
        country_code_length = len(country['code'])
        number_length = len(number)
        if number_length == country_code_length + country_codes[prefix]['min_length']:
            print(f"The mobile number belongs to {country['name']} ({country['code']}).")
            print("The number is valid.")
        else:
            print(f"The mobile number does not match the expected length for {country['name']} ({country['code']}).")
            print("Please check the number.")
    else:
        print("Country not found for the given mobile number.")

if __name__ == "__main__":
    country_codes = {
        '91': {'name': 'India', 'code': '+91', 'min_length': 10},
        '1': {'name': 'United States', 'code': '+1', 'min_length': 10},
        '44': {'name': 'United Kingdom', 'code': '+44', 'min_length': 10},
        '81': {'name': 'Japan', 'code': '+81', 'min_length': 10},
        '86': {'name': 'China', 'code': '+86', 'min_length': 11},
        '49': {'name': 'Germany', 'code': '+49', 'min_length': 11},
        '33': {'name': 'France', 'code': '+33', 'min_length': 9},
        '7': {'name': 'Russia', 'code': '+7', 'min_length': 10},
        '55': {'name': 'Brazil', 'code': '+55', 'min_length': 11},
        '61': {'name': 'Australia', 'code': '+61', 'min_length': 9},
    }

    mobile_number = input("Enter the mobile number: ")

    identify_country_and_validate(mobile_number, country_codes)
