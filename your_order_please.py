def order(sentence):
    if not sentence:
        return ""
    
    palavras = sentence.split()
    position = {}
    
    for palavra in palavras:
        for char in palavra:
            if char.isdigit():
                pos = int(char)
                position[pos] = palavra
    
    # Para obter a ordem correta, você pode percorrer de 1 a 9 e coletar as palavras
    resultado = []
    for i in range(1, len(position) + 1):
        resultado.append(position[i])
    
    return " ".join(resultado)

# Testando as funções
print(order("is2 Thi1s T4est 3a"))  # Esperado: "Thi1s is2 3a T4est"
print(order("4of Fo1r pe6ople g3ood th5e the2"))  # Esperado: "Fo1r the2 g3ood 4of th5e pe6ople"
print(order(""))  # Esperado: ""



