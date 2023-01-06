def check_password(password):
    # Check if password is at least 8 characters long
    if len(password) < 8:
        return 'Password must be at least 8 characters long'
    # Check if password contains at least one digit
    elif not any(char.isdigit() for char in password):
        return 'Password must contain at least one digit'
    # Check if password contains at least one uppercase letter
    elif not any(char.isupper() for char in password):
        return 'Password must contain at least one uppercase letter'
    # Check if password contains at least one lowercase letter
    elif not any(char.islower() for char in password):
        return 'Password must contain at least one lowercase letter'
    # If all checks pass, password is considered valid
    else:
        return 'Password is ok'

# Prompt user to enter password
password = input('Enter your password: ')

# Check the password and print the result
print(check_password(password))
