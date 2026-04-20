def get_password():
    return input("""
                                                                                                                      
█████▄  ▄▄▄   ▄▄▄▄  ▄▄▄▄ ▄▄   ▄▄  ▄▄▄  ▄▄▄▄  ▄▄▄▄    ▄████▄ ▄▄  ▄▄  ▄▄▄  ▄▄  ▄▄ ▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄  
██▄▄█▀ ██▀██ ███▄▄ ███▄▄ ██ ▄ ██ ██▀██ ██▄█▄ ██▀██   ██▄▄██ ███▄██ ██▀██ ██  ▀███▀   ▄█▀ ██▄▄  ██▄█▄ 
██     ██▀██ ▄▄██▀ ▄▄██▀  ▀█▀█▀  ▀███▀ ██ ██ ████▀   ██  ██ ██ ▀██ ██▀██ ██▄▄▄ █   ▄██▄▄ ██▄▄▄ ██ ██ 
                                                                                                      
                 Insert your password here: """)

def get_password_length(password):
    return len(password)

def get_character_diversity(password):
    return {
        "number": any(c.isdigit() for c in password),
        "character": any(c.isalpha() for c in password),
        "symbol": any(not c.isalnum() for c in password),
        "uppercase": any(c.isupper() for c in password),
        "lowercase": any(c.islower() for c in password),
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