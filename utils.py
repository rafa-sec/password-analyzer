points = 0

def get_password():
    return input("""
                                                                                                     
                                                                                                     
█████▄  ▄▄▄   ▄▄▄▄  ▄▄▄▄ ▄▄   ▄▄  ▄▄▄  ▄▄▄▄  ▄▄▄▄    ▄████▄ ▄▄  ▄▄  ▄▄▄  ▄▄  ▄▄ ▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄  
██▄▄█▀ ██▀██ ███▄▄ ███▄▄ ██ ▄ ██ ██▀██ ██▄█▄ ██▀██   ██▄▄██ ███▄██ ██▀██ ██  ▀███▀   ▄█▀ ██▄▄  ██▄█▄ 
██     ██▀██ ▄▄██▀ ▄▄██▀  ▀█▀█▀  ▀███▀ ██ ██ ████▀   ██  ██ ██ ▀██ ██▀██ ██▄▄▄ █   ▄██▄▄ ██▄▄▄ ██ ██ 
                                                                                                      
                 Insert your password here: """)

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

def has_too_many_repeats(password, max_repeats=2):
    count = 1

    for i in range(1, len(password)):
        if password[i] == password[i - 1]:
            count += 1
            if count > max_repeats:
                return True
        else:
            count = 1

    return False

def set_password_points(password_length, password_diversity, points, password):
    if password_length < 8 :
        points -= 1
    elif password_length <= 12:
       points += 1
    elif password_length <= 14:
        points += 2
    elif password_length > 14:
        points += 3
        
    if password_diversity["number"] and password_diversity["character"]:
        points += 2
    elif password_diversity["number"]:
        points += 1
    

    if password_diversity["symbol"]:
        points += 1

    if password_diversity["uppercase"] and password_diversity["lowercase"]:
        points += 1
    elif password_diversity["uppercase"]:
        points -= 1
    elif password_diversity["lowercase"]:
        points -= 1


    if has_too_many_repeats(password):
        points -= 3

    return points
