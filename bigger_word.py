def bigger_word(frase):
    l = []
    palavras = frase.split()
    for palavra in palavras:
        l.append((palavra, len(palavra)))
    
    maior_palavra = l[0]
    
    for palavra in l:
       if palavra[1] > maior_palavra[1]:
           maior_palavra = palavra
    return 'maior palavra: ' + maior_palavra[0]

print(bigger_word('the quick brown fox jumps'))
print(bigger_word('hello world this is a test'))
