import string
import re


def check_password(password):
    if len(password) < 8:
        return print('password is too short')
    has_lower = re.search(r'[a-z]', password)
    has_upper = re.search(r'[A-Z]', password)
    has_digits = re.search(r'\d', password)
    has_punctuation = re.search(r'\W_', password)
    if not (has_digits and has_lower and has_punctuation and has_upper):
        return print('Password must contain: uppercase, lowercase, digits, and special chars')
    return print('success')


def check_password_second(password):
    if len(password) < 8:
        return 'Password is too short'

    has_upper = any(c in string.ascii_uppercase for c in password)
    has_lower = any(c in string.ascii_lowercase for c in password)
    has_digit = any(c in string.digits for c in password)
    has_special = any(c in string.punctuation for c in password)

    if not all([has_upper, has_lower, has_digit, has_special]):
        return 'Password does not meet requirements'

    return 'Success'


password = input("enter the password:  ")
print('\n')

check_password(password)
print('\n')

print(check_password_second(password))
