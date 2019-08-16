import datetime
from main import *

def real_age(number_of_days):
    if number_of_days < 30:
        years = 0
        months = 0
        return f"{years} years and {months} months old"
    elif 30 < number_of_days < 365:
        years = 0
        months = 365 // 30
        return f"{years} years and {months} months old"
    elif number_of_days > 365:
        years = number_of_days // 365
        months = (number_of_days % 365) // 30
        return f"{years} years and {months} months old"
    else:
        return f"Some error occured."
print("\n")      
today = datetime.date.today()
for child in children_list:
    print(f"Child {child.last_name} {child.first_name} is {real_age((today - child.birthdate).days)}")