from utils import get_password, get_password_length, get_character_diversity,set_password_points, points
from analyzer import  set_password_status


#Base variables

password = get_password()
password_length = get_password_length(password)
password_diversity = get_character_diversity(password)
points = set_password_points(password_length, password_diversity, password)
password_status = set_password_status(points)


print(f"""
Your password: {password}
Length: {password_length}
Strength: {password_status}
Password points: {points}

Character diversity: {password_diversity}
""")
