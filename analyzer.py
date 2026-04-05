def set_password_status(password_length):
    if password_length < 8:
        return "Weak"
    elif password_length <= 12:
        return "Okay"
    elif password_length <= 14:
        return "Strong"
    else:
        return "Very Strong"