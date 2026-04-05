from utils import get_password, get_password_length
from analyzer import set_password_status

password = get_password()
password_length = get_password_length(password)

status = set_password_status(password_length)

print(f"""
Your password: {password}
Length: {password_length}
Strength: {status}
""")