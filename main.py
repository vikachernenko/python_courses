# import random

# print(random.choice('sdqefqwfeqf'))
# print(random.choices('sdqefqwfeqf', k=3))

# my_list = [231, 32, 323, 33, 32, 3]
# print(random.shuffle(my_list))
# print(my_list)

# print(''.join(random.choices('0123456789zxcvbnmasdfghjklqwertyuiop', k=8)))


import secrets
import string

all_chars = string.ascii_letters+string.digits+string.punctuation

print(''.join(secrets.choice(all_chars) for i in range(20)))
