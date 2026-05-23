import random
import string

print("===== Strong Password Generator =====")

length = int(input("Enter password length: "))

if length < 6:
    print("Password length should be at least 6")
else:
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    all_characters = uppercase + lowercase + digits + symbols

    password = ""

    password += random.choice(uppercase)
    password += random.choice(lowercase)
    password += random.choice(digits)
    password += random.choice(symbols)

    for i in range(length - 4):
        password += random.choice(all_characters)

    password_list = list(password)
    random.shuffle(password_list)

    final_password = "".join(password_list)

    print("Generated Strong Password:", final_password)