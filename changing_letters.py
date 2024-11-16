def swap(st):
    vogais = ['a', 'e', 'i', 'o' , 'u']
    palavra = []

    for n in st:
        if n in vogais:
            palavra.append(n.upper())
        else:
            palavra.append(n)

    return ''.join(palavra)
        

print(swap("HelloWorld!")), "HEllOWOrld!"
print(swap("Sunday")), "SUndAy"
print(swap("Codewars")),"COdEwArs"
print(swap("Monday")), "MOndAy"
print(swap("Friday")), "FrIdAy"
print(swap("abracadabra")), "AbrAcAdAbrA"