import secrets
import time
def generate_password(len, chars):
    passwords = []
    password = ''
    for circle in range(num):
        for symbol in range(len):
            password += secrets.choice(chars)
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
        flag_nums = input('Include numbers? (y n)\n')
        flag_lowers = input('Include lowercase letters? (y n)\n ')
        flag_uppers = input('Include uppercase letters? (y n)\n ')
        flag_symbols = input('Include special symbols? (y n)\n ')
        flag_complex = input('Include confusing letters, like "il1Lo0O"? (y n)\n')
    except ValueError:
        print('This one should be a number. Try again\n')
        continue
    chars += digits if flag_nums.lower() == 'y' else ''
    chars += lowercase_letters if flag_lowers.lower() == 'y' else ''
    chars += uppercase_letters if flag_uppers.lower() == 'y' else ''
    chars += punctuation if flag_symbols.lower() == 'y' else ''
    chars += complex if flag_complex.lower() == 'y' else ''
    print('Password can`t be empty lol XD') if chars == '' else print('\n' + generate_password(len, chars) + '\n')

    exit = input('Run again? Type "n" to exit\n')
    if exit.lower() == 'n':
        break
    else:
        continue
print('See ya!')
time.sleep(2)