import string
import re


def check_password(password):
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


while True:
    password = input('enter the password')
    information_res = check_password(password)
    if information_res[0]:
        print(information_res[1])
        break
    print(information_res[1])
