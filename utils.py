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
