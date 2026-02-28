import os

from dotenv import load_dotenv

# load environment variables from the .env
load_dotenv()

EMAIL_PASSWD = os.getenv("EMAIL_PASSWORD")
EMAIL_ADDR = os.getenv("EMAIL_ADDR")


print(f"email password {EMAIL_PASSWD}")
print(f"email address {EMAIL_ADDR}")
