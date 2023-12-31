def minimum_characters_to_add(password):
    def is_strong(p):
        has_digit = any(c.isdigit() for c in p)
        has_lowercase = any(c.islower() for c in p)
        has_uppercase = any(c.isupper() for c in p)
        has_special = any(c in "!@#$%^&*()-+" for c in p)
        return len(p) >= 8 and has_digit and has_lowercase and has_uppercase and has_special

    missing_digit = not any(c.isdigit() for c in password)
    missing_lowercase = not any(c.islower() for c in password)
    missing_uppercase = not any(c.isupper() for c in password)
    missing_special = not any(c in "!@#$%^&*()-+" for c in password)

    min_digit = 1 if missing_digit else 0
    min_lowercase = 1 if missing_lowercase else 0
    min_uppercase = 1 if missing_uppercase else 0
    min_special = 1 if missing_special else 0

    return max(0, 8 - len(password), min_digit + min_lowercase + min_uppercase + min_special)

password = input("Enter the password: ")
additional_chars = minimum_characters_to_add(password)
print(f"Minimum characters to add: {additional_chars}")
