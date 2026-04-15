def set_password_status(points):
    if points <= 0:
        return "Extremely weak password"
    elif points <= 1:
        return "Very weak password"
    elif points <= 2:
        return "Weak password"
    elif points <= 3:
        return "Okay"
    elif points <= 6:
        return "Good"
    elif points <= 8:
        return "Strong"
    elif points >= 10:
        return "Very strong"
