def square_digits(num):
    quadrados = []
    for n in str(num):
        quadrados += str(int(n) ** 2)
    return ''.join(quadrados)

print(square_digits(9119)) # 811181
print(square_digits(765)) # 493625