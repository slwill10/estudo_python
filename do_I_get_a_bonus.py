def bonus_time(salary, bonus):
    if bonus:
        return f"${salary * 10}"
    else:
        return f"${salary}"



print(bonus_time(10000, True)), '$100000'
print(bonus_time(25000, True)), '$250000'
print(bonus_time(10000, False)), '$10000'
print(bonus_time(60000, False)), '$60000'
print(bonus_time(2, True)), '$20'
print(bonus_time(78, False)), '$78'
print(bonus_time(67890, True)), '$678900'