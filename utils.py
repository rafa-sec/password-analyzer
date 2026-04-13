points = 0

def get_password():
    return input("Insert your password here: ")

def get_password_length(password):
    return len(password)

def get_character_diversity(s):
    return {
        "number": any(c.isdigit() for c in s),
        "character": any(c.isalpha() for c in s),
        "symbol": any(not c.isalnum() for c in s),
        "uppercase": any(c.isupper() for c in s),
        "lowercase": any(c.islower() for c in s),
}

def set_password_points(password_length, password_diversity, points):
    if password_length < 8 :
        points -= 1
    elif password_length <= 12:
       points += 0 
    elif password_length <= 14:
        points += 2
    elif password_length > 14:
        points += 3
        
    if password_diversity["number"]:
       points += 1
    if password_diversity["character"]:
       points += 1
    if password_diversity["symbol"]:
       points += 1
    if password_diversity["uppercase"]:
        points += 1
    if password_diversity["lowercase"]:
        points += 1

    return points
