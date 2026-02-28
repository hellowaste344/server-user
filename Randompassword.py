import secrets
import string


def generate_secure_Password(
    use_digits=True, use_symbols=True, use_letters=True, length=16
):
    characters = ""
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    if use_letters:
        characters += string.ascii_letters
    print("strong password")

    StrongPassword = "".join(secrets.choice(characters) for i in range(length))

    with open("Password.txt", "w") as f:
        f.write(StrongPassword)

    return StrongPassword
