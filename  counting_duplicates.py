def duplicate_count(text):
    armazena = []
    rep = set()
    for n in text.lower():
        if n in armazena:
            rep.add(n)
        else:
            armazena.append(n)

    print(len(rep))

duplicate_count(""), 0
duplicate_count("abcde"), 0
duplicate_count("abcdeaa"), 1
duplicate_count("abcdeaB"), 2
duplicate_count("Indivisibilities"), 2