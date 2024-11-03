def hero(bullets, dragons):
    qtd = int(dragons) * 2
    if qtd > bullets:
        return False
    else:
        return True
    print(qtd)

print(hero(10, 5)), True
print(hero(7, 4)), False
print(hero(4, 5)), False
print(hero(100, 4)), True
print(hero(1500,751)), False
print(hero(0, 1)), False