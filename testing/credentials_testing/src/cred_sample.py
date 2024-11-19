import re

def get_email_from_input():
    """ Contains '@' and '.' """
    email = input("Tell me your email: ")

    if ("@" not in email or "." not in email):
        print('Email is not valid.')
    else:
        return email
    
def get_username_from_input():
    """ Not empty and no spaces """
    username = input("Tell me your username: ")

    if (username == '' or ' ' in username):
        print('Username is not valid.')
    else:
        return username
    
def get_password_from_input():
    """ Password needs to be at least 8 characters long with at least one number, one special character and one letter. """
    pw = input("Create your password: ")

    if (len(pw) < 8 or not re.search(r'[a-zA-Z]', pw) \
        or not re.search(r'\d', pw) or \
            not re.search(r'[!@#$%^&*(),.?":{}|<>]', pw)):
        print('Password is not valid.')
    else:
        return pw