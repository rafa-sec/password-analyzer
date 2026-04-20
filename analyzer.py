from utils import has_too_many_repeats, contains_common_word, has_sequence, has_year_pattern

def calculate_password_points(password_length, password_diversity, password):
    points = 0
    feedback = []

    if contains_common_word(password):
        points -= 5
        feedback.append("Avoid common words")

    if has_sequence(password):
        points -= 3
        feedback.append("Avoid sequences")

    if has_year_pattern(password):
        points -= 3
        feedback.append("Avoid using years")

    if password_length < 8:
        points -= 1
    elif password_length <= 12:
        points += 1
    elif password_length <= 14:
        points += 2
    else:
        points += 5

    if password_diversity["number"] and password_diversity["character"]:
        points += 2
    elif password_diversity["number"]:
        points += 1


    if password_diversity["symbol"]:
        points += 1
        
    
    if password_diversity["uppercase"] and password_diversity["lowercase"]:
        points += 2
    elif password_diversity["uppercase"] or password_diversity["lowercase"]:
        points -= 1
        

    if has_too_many_repeats(password):
        points -= 5
        feedback.append("Too many characters repeated!")




    ###FEEDBACK AREA####

    if not password_diversity["uppercase"]:
        feedback.append("Add uppercase letters")

    if not password_diversity["lowercase"]:
        feedback.append("Add lowercase letters")

    if not password_diversity["symbol"]:
        feedback.append("Add symbols")
    
    if not password_diversity["character"]:
        feedback.append("Add characters")

    if not password_diversity["number"]:
        feedback.append("Add numbers")

    return points, feedback


def get_password_status(points):
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
    elif points <= 9:
        return "Strong"
    else:
        return "Very strong"
