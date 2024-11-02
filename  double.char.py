def double_char(s):
    contador = []
    
    for l in s:
            contador.append(l * 2)
    print(''.join(contador))

double_char("String")