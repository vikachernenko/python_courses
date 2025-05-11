import string
import re


def check_password_third(password):
    # проверяем что в строке минимум 8 символов, знаки tab и переходы на новую строку не считаются -  \S
    len_pattern = re.compile(r'\S{8,}')
    lowercase_pattern = re.compile(r'^.*[a-z]+.*$')
    uppercase_pattern = re.compile(r'^.*[A-Z]+.*$')
    digits_pattern = re.compile(r'^.[0-9]+.*$')
    punctuation_pattern = re.compile(r'^.*[!@#$%^&*]+.*$')

    if not re.fullmatch(len_pattern, password):
        return (False, 'password is too short')
    if not re.fullmatch(lowercase_pattern, password):
        return (False, 'password must have at least one lowercase letter')
    if not re.fullmatch(uppercase_pattern, password):
        return (False, 'password must have at least one uppercase letter')
    if not re.fullmatch(digits_pattern, password):
        return (False, 'password must have at least one digit')
    if not re.fullmatch(punctuation_pattern, password):
        return (False, 'password must have at least one puncuation symbol !@#$%^&*')
    return (True, 'Success :) ')


# def check_password(password):
#     if len(password) < 8:
#         return print('password is too short')
#     has_lower = re.search(r'[a-z]', password)
#     has_upper = re.search(r'[A-Z]', password)
#     has_digits = re.search(r'\d', password)
#     has_punctuation = re.search(r'\W_', password)
#     if not (has_digits and has_lower and has_punctuation and has_upper):
#         return print('Password must contain: uppercase, lowercase, digits, and special chars')
#     return print('success')


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


print(check_password_third('123'))
print(check_password_third('12345678'))
print(check_password_third('1234567a'))
print(check_password_third('123456Ba'))
print(check_password_third('asdbADGAG'))
print(check_password_third('3234sfASDF'))
print(check_password_third('asdfASDF3242!&'))
