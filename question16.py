import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z]\w*([.][_a-zA-Z0-9]+)*@[a-zA-Z0-9]+([.][a-zA-Z0-9]+)*[a-zA-Z0-9]$'
    return re.match(pattern, email) is not None and email.count('.') <= 1

# Input email address
email_address = input("Enter an email address: ")

# Check validity
if is_valid_email(email_address):
    print("The email address is valid.")
else:
    print("The email address is not valid.")
