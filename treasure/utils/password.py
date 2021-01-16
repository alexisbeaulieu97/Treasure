from getpass import getpass


def create_password(password_type, max_retries=3):
    password = ''
    password_verif = ''
    retry_count = 1
    while True:
        password = getpass(f'Create a {password_type} password: ')
        password_verif = getpass(f'Re-enter {password_type} password: ')
        if password != password_verif:
            print(
                f'Provided passwords were different... ({retry_count}/{max_retries})')
            retry_count = retry_count + 1
        else:
            break
        if retry_count > max_retries:
            print(f'Failed to create {password_type} password, exiting...')
            exit()
    return password


def get_password(password_type=None):
    password_type = password_type or 'your'
    return getpass(f'Enter {password_type} password: ')
