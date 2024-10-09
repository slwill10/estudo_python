def get_count(sentence):
    count = 0
    vogais = ['a', 'e', 'i', 'o', 'u']
    for letra in sentence:
        if letra in vogais:
            count+=1
    return count
get_count('bcdfghjklmnpqrstvwxz y')
get_count('abracadabra')

