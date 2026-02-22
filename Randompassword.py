import random
import string


def generatePassword(length=12):
    character = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(character) for _ in range(length))
    print("weak password")
    with open("password1.exe", "w") as f:
        f.write(password)
    return password


print(generatePassword(10))
#####################

import secrets
import string


def generate_secure_Password(length=16, use_digits=True, use_symbols=True):
    character = string.ascii_letters
    if use_digits:
        character += string.digits
    if use_symbols:
        character += string.punctuation
    print("strong password")

    StrongPassword = "".join(secrets.choice(character) for i in range(length))

    with open("Password.text", "w") as f:
        f.write(StrongPassword)

    return StrongPassword


print(generate_secure_Password(length=10))
