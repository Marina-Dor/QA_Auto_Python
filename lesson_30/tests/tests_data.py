import random
import string


def generate_random_email():
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"tester_{random_string}@testemail.com"


registration_query = {
    "first_name": "Maryna",
    "last_name": "Dor",
    "email": generate_random_email(),
    "password": "Password_123",
    "repeat_password": "Password_123"
}

