def abbrev_name(name):
    separadas = name.split()
    print(separadas)

    primeira = separadas[0][0].upper()
    segunda = separadas[1][0].upper()

    return f'{primeira}.{segunda}'
   
print(abbrev_name("Sam Harris")), "S.H"
# abbrev_name("patrick feenan"), "P.F"
# abbrev_name("Evan C"), "E.C"
# abbrev_name("P Favuzzi"), "P.F"
# abbrev_name("David Mendieta"), "D.M"