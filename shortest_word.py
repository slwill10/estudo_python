def find_short(s):
    l = []
    frases = s.split()
    for i in frases:
        l.append((i, len(i)))

    menor_palavra = l[0] 

    for palavra in l:
        if palavra[1] < menor_palavra[1]:
            menor_palavra = palavra


    return len(menor_palavra[0])

print(find_short("bitcoin take over the world maybe who knows perhaps"))
# find_short("turns out random test cases are easier than writing out basic ones")
# find_short("lets talk about javascript the best language")
# find_short("i want to travel the world writing code one day")
# find_short("Lets all go on holiday somewhere very cold") 
# find_short("Let's travel abroad shall we")