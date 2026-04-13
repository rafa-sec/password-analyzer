def set_password_status(points):
    if points < 0:
        return "Very weak password"
    elif points == 0:
        return "Weak password"
    elif points == 2:
        return "Okay, but could be better"
    elif points <= 3:
        return "Okay"
    elif points <= 5:
        return "Good"
    elif points <= 7:
        return "Strong"
    elif points > 8:
        return "Very strong"
