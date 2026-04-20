#Simple common words database for analysis
COMMON_WORDS = [
    "password", "admin", "user", "login",
    "rafael", "john", "maria", "alex",
    "qwerty", "abc123", "welcome"
]



#Get password function
def get_password():
    return input("""
                                                                                                                      
█████▄  ▄▄▄   ▄▄▄▄  ▄▄▄▄ ▄▄   ▄▄  ▄▄▄  ▄▄▄▄  ▄▄▄▄    ▄████▄ ▄▄  ▄▄  ▄▄▄  ▄▄  ▄▄ ▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄  
██▄▄█▀ ██▀██ ███▄▄ ███▄▄ ██ ▄ ██ ██▀██ ██▄█▄ ██▀██   ██▄▄██ ███▄██ ██▀██ ██  ▀███▀   ▄█▀ ██▄▄  ██▄█▄ 
██     ██▀██ ▄▄██▀ ▄▄██▀  ▀█▀█▀  ▀███▀ ██ ██ ████▀   ██  ██ ██ ▀██ ██▀██ ██▄▄▄ █   ▄██▄▄ ██▄▄▄ ██ ██ 
                                                       
                                                                                                      
                 Insert your password here: """)


#Return password length
def get_password_length(password):
    return len(password)


#Get Character diversity
def get_character_diversity(password):
    return {
        "number": any(c.isdigit() for c in password),
        "character": any(c.isalpha() for c in password),
        "symbol": any(not c.isalnum() for c in password),
        "uppercase": any(c.isupper() for c in password),
        "lowercase": any(c.islower() for c in password),
    }


#Detect if there is a character being repeated in the password
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



#Detect common patterns system
def contains_common_word(password):
    password_lower = password.lower()

    for word in COMMON_WORDS:
        if word in password_lower:
            return True

    return False

def has_sequence(password):
    sequences = ["123", "abc", "qwerty"]

    password_lower = password.lower()

    for seq in sequences:
        if seq in password_lower:
            return True

    return False


def has_year_pattern(password):
    for year in range(1900,2031):
        if str(year) in password:
            return True
    return False
