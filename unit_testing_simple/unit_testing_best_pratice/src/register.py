import re

def validate_username(username):
    """Check if the username is valid (not empty, no spaces)."""
    if not username or " " in username:
        return False
    return True

def validate_email(email):
    """Check if the email contains '@' and '.' """
    return "@" in email and "." in email

def validate_password(password):
    """Check if the password meets security requirements."""
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):  # At least one number
        return False
    if not any(char.isalpha() for char in password):  # At least one letter
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):  # At least one special character
        return False
    return True

def register_user(username, email, password):
    """Validate all fields and return True if registration is successful."""
    if not validate_username(username):
        return "Invalid username"
    if not validate_email(email):
        return "Invalid email"
    if not validate_password(password):
        return "Invalid password"
    return "Registration successful"

