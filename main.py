import re
import random
import string

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

def generate_random_string(length=5):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def generate_gmail_variations(email, count):
    if not validate_email(email):
        print("The entered email is invalid.")
        return []
    
    local_part, domain = email.split("@")
    if domain != "gmail.com":
        print("This tool only works for Gmail addresses.")
        return []
    
    variations = []
    for i in range(count):
        random_part = generate_random_string()
        variations.append(f"{local_part}+{random_part}{i}@{domain}")
    return variations

input_email = input("Enter your email: ")
try:
    count = int(input("Enter the number of variations: "))
    generated_emails = generate_gmail_variations(input_email, count)
    if generated_emails:
        print("Generated variations:")
        for email in generated_emails:
            print(email)
        with open("generated_emails.txt", "w") as file:
            file.write("\n".join(generated_emails))
        print("The variations have been saved to 'generated_emails.txt'.")
except ValueError:
    print("Please enter a valid number.")
