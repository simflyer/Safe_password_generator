import random
import time
def generate_password(len, chars):
    passwords = []
    password = ''
    for circle in range(num):
        for symbol in range(len):
            password += random.choice(chars)
        passwords.append(password)
        password = ''
    return '\n'.join(passwords)



#constant
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
complex = 'il1Lo0O'
chars = ''

while True:
    try:
        num = int(input('How many passwords?\n '))
        len = int(input('Password length?\n '))
        flag_nums = input('Include numbers? (yes no)\n')
        flag_lowers = input('Include lowercase letters? (yes no)\n ')
        flag_uppers = input('Include uppercase letters? (yes no)\n ')
        flag_symbols = input('Include special symbols? (yes no)\n ')
        flag_complex = input('Include confusing letters, like "il1Lo0O"? (yes no)\n')
    except ValueError:
        print('This one should be a number. Try again\n')
        continue
    chars += digits if flag_nums.lower() == 'yes' else ''
    chars += lowercase_letters if flag_lowers.lower() == 'yes' else ''
    chars += uppercase_letters if flag_uppers.lower() == 'yes' else ''
    chars += punctuation if flag_symbols.lower() == 'yes' else ''
    chars += complex if flag_complex.lower() == 'yes' else ''
    print('Password can`t be empty lol XD') if chars == '' else print(generate_password(len, chars))
    print()
    exit = input('Run again? Type "no" to exit\n')
    if exit.lower() == 'no':
        break
    else:
        continue
print('See ya!')
time.sleep(2)